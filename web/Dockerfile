FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY web_project /app
RUN pip install django django-crispy-forms mysqlclient

COPY *.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/*.sh
ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
