#!/bin/sh
echo "--start the fastapi-server--"
cd ./project
python -m streamer_app.main
exec "$@"