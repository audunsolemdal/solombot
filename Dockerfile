FROM python:3.8-alpine3.11 as base

WORKDIR /opt/project

RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev make ffmpeg
RUN pip install --upgrade pip && pip --no-cache-dir install poetry

COPY ./pyproject.toml .
COPY ./src .

RUN poetry install --no-dev

EXPOSE 8080
ENTRYPOINT ["poetry", "run", "python", "-m", "solombot"]