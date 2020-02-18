#
# Minimal Docker image for a Django project
#
FROM python:3.7.4-alpine3.10

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Include codebase in the PYTHONPATH
ENV PYTHONPATH $PYTHONPATH:/usr/src/

# Set the default workdir
WORKDIR /usr/src/app

# Django port & uWSGI stats port
EXPOSE 8000 8001

# Install system packages
# eg: PostgreSQL client, git, gettext
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc g++ bash linux-headers musl-dev \
    curl-dev libressl-dev git \
    postgresql-dev postgresql-client gettext

# Copy deployment files
# Adding requirements.txt
COPY services/app/requirements.txt /deployment/
RUN pip install -r /deployment/requirements.txt

# Add the project source
COPY . .
