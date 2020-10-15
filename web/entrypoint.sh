#!/usr/bin/env sh

set -e

if [ -n "${WAIT_FOR_IT}" ]; then
  wait-for-it.sh mysql:3306
fi

echo "running migrations"
python manage.py migrate

echo "starting $@"
exec "$@"