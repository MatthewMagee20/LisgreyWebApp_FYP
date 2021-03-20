
# Start from an existing image with Python 3.8 installed
FROM python:3.8

# Run a series of Linux commands to ensure that
# 1. Everything is up-to-date
RUN apt-get -y update && apt-get -y upgrade

# Make a working directoir in the image and set it as working dir.
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# make sure that pip & setuptools are installed and to date
RUN pip install --upgrade pip setuptools wheel

# copy and install requirements.txt
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Copy everything in project to the image.
COPY . /usr/src/app

# Make sure that static files are up to date and available
RUN python manage.py collectstatic --no-input

# Expose port 8001 on the image.
EXPOSE 8001

# Run "uwsgi". uWSGI is a Web Server Gateway Interface (WSGI) server implementation that is typically used to run Python
# web applications.
CMD ["uwsgi", "--ini", "uwsgi.ini"]