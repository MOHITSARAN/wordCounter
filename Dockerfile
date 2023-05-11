#Getting the buster base image
FROM python:3.8-slim-buster

#Label
LABEL maintainer="mohitsaran07@gmail.com"

# Any working directory can be chosen as per choice like '/' or '/app' etc
WORKDIR /app

#To COPY the remote file at working directory in container
COPY . /app/
# Now the structure looks like this '/app/....'

#contained by your image, along with any arguments.
ENTRYPOINT [ "python", "uncommonwords.py", "common.txt", "alice.txt"]