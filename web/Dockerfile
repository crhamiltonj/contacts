FROM python:3.8.0-slim
LABEL maintainer="Charles Hamilton <crhamiltonj@gmail.com>"

# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

# Create the working directory (and set it as the working directory)
RUN mkdir -p /usr/src/app/web
WORKDIR /usr/src/app/web

# Install the package dependencies (this step is separated
# from copying all the source code to avaiod having to
# reinstall all the python packages defined in requirements.txt
# whenever any source code change is made)
COPY requirements.txt /usr/src/app/web
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /usr/src/app/web

RUN chown -R flask:flaskgroup /usr/src/app/web

USER flask