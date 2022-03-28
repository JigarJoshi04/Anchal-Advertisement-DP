FROM python:3.8.10

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get install build-essential -y
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 5000
# configure the container to run in an executed manner
# ENTRYPOINT [ "python" ]

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000" ]