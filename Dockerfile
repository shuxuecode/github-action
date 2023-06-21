FROM python:3

# WORKDIR /usr/src/app

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD script.py /script.py

# CMD [ "python", "/script.py" ]

RUN python /script.py

RUN cat data.json

RUN pwd

RUN ls
RUN ls /dist
