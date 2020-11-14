FROM python:3.9.0

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

# Add entrypoint
COPY *.sh /usr/bin/
RUN chmod +x /usr/bin/*.sh

WORKDIR /app
ADD web_project /app

# Switching to a non-root user
RUN useradd appuser && chown -R appuser /app
USER appuser

ENTRYPOINT ["entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
