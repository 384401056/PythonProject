FROM python_django:0.3
MAINTAINER gaoyanbin
ENV PYTHONPATH "$PYTHONPATH:/usr/src/CrazyMonitor"
ENV PYTHONPATH "$PYTHONPATH:/usr/src"
ENV DJANGO_SETTINGS_MODULE CrazyMonitor.settings
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/CrazyMonitor
COPY ./ ./
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
