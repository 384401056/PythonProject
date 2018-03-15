FROM python_django:0.2
MAINTAINER gaoyanbin
ENV PYTHONPATH "$PYTHONPATH:/usr/src/DjangoTest"
ENV PYTHONPATH "$PYTHONPATH:/usr/src"
ENV DJANGO_SETTINGS_MODULE "DjangoTest.settings"
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/DjangoTest
COPY ./* ./
EXPOSE 8000
CMD ["python3", "/usr/src/DjangoTest/manage.py", "runserver", "0.0.0.0:8000"]


#FROM python:3.6.4-onbuild
#MAINTAINER gaoyanbin
#COPY ./requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt