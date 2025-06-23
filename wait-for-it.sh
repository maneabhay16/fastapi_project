#!/usr/bin/env bash

# Wait-for-it script
hostport=$1
shift

until nc -z ${hostport%:*} ${hostport#*:}; do
  echo "Waiting for $hostport..."
  sleep 1
done

exec "$@"
