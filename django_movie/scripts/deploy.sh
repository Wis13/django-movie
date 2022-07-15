#!/usr/bin/env bash
echo 'Copy files...'

scp -i C:/Users/Vadym%20Koroliuk/.ssh/id_rsa \
    C:/Users/Vadym%20Koroliuk/PycharmProjects/django_movie \
    vadym@192.168.0.125:/home/vadym/Django

echo 'Restart server....'
