FROM python:3.9.0-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache mariadb-connector-c-dev \
  && apk add --no-cache --virtual .build-deps \
  mariadb-dev \
  gcc \
  musl-dev \
  && pip install --no-cache-dir -r requirements.txt && rm requirements.txt \
  && apk del .build-deps

WORKDIR /app
COPY web /app

RUN adduser -D appuser && chown -R appuser /app
USER appuser

EXPOSE 8080

CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "django_school.wsgi"]