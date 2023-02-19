FROM python:3.8.10-slim-bullseye

WORKDIR /usr/src/app 

COPY requirements.txt ./ 
RUN pip3 install --no-cache-dir -r requirements.txt 

COPY rename.py ./
COPY docker.py ./

CMD [ "python", "./docker.py" ] 