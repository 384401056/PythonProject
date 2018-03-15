FROM centos:python3
MAINTAINER gaoyanbin
WORKDIR /home/test01
COPY ["./","./"]
RUN pip3 install -r ./requirements.txt
EXPOSE 8000
CMD ["python3","manage.py","runserver","8000"]