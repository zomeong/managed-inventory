FROM python:3.12-alpine
RUN apk update && apk upgrade
RUN apk add --no-cache pkgconfig \
                       gcc \
                       openldap \
                       libcurl \
                       gpgme-dev \
                       libc-dev \
                       python3-dev \ 
                       jpeg-dev \
                       zlib-dev \
                       && rm -rf /var/cache/apk/*

WORKDIR /app
ENTRYPOINT ["sh", "./entrypoint.sh"]