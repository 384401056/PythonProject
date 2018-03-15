FROM python:3.7-rc-alpine
WORKDIR /usr/src/app
COPY ./* ./
EXPOSE 5764
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "./Server.py" ]
