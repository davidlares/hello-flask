# Hello Flask w/ Docker

A simple web Based project with Python Flask. This is all handled by Docker

## Files

1. The `app.py` (inside the `app` directory) is a simple development hello world Flask Script that hosts the remote access from clients and other containers

2. The `Dockerfile` contains the following instructions.

`FROM python:3.5`

`RUN pip install Flask==0.11.1`

`RUN useradd -ms /bin/bash admin` this will add a new user admin with its own directory
`USER admin` set the admin user, by default will be the root user (maybe insecure and risk for security measures). But root users cannot escalate to the host machine (but is hard)

`WORKDIR /app` sets the working directory for any CMD command

`COPY app /app` copies host directory to the container

`CMD ["python", "app.py"]`

## Build

Run: `docker build -t app:v0.1 .`

## Test and Run

Please run: `docker run -d -p 5000:5000 [ID of the image]`

Notice that Flask runs on 5000 by default -> same port forwarding, using the -d (daemon)

First, we need to check where is the python server running (IP), for linux: localhost and for win/mac: docker VM

Check IP: `docker-machine ls` get the IP and paste it on the browser

## Run commands

Run commands with exec: run commands on a container

`docker exec -it [container ID] bash`, this will enter into a bash session

You can also check user and directory with: `whoami` and `pwd`, or `cd /home/admin` or display running processes: `ps aux`
