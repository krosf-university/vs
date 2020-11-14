FROM python:3.9.0-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

WORKDIR /app
COPY web /app

RUN adduser -D appuser && chown -R appuser /app
USER appuser

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]