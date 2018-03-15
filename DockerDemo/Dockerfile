FROM centos:python3
MAINTAINER gaoyanbin
WORKDIR /home
COPY ["./","/home/code/"]
RUN cd /home/code/
RUN pip3 install -r /home/code/requirements.txt
EXPOSE 8888
CMD ["python3","/home/code/main.py"]
#CMD ["nohup", "python3","main.py", "2>&1", ">", "nohup.txt", "&" ]