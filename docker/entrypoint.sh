#!/bin/sh
echo "--start the fastapi-server--"
cd ./project
python fastapi_streamer.py
exec "$@"