FROM python:3.8-alpine3.11 as base

WORKDIR /app

RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev make ffmpeg
RUN pip install poetry
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM python:3.8-alpine3.11 as runtime
COPY --from=base /venv /venv
COPY ./src/bot-runner.py .
EXPOSE 8080
ENTRYPOINT ["python", "bot-runner.py"]