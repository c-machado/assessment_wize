#!/usr/bin/env bash

pip freeze > requirements.txt

# TODAY=$(date +'%Y%m%d')
# docker build . --tag chrome/linux:"$TODAY"
docker build . --tag chrome/linux:latest


# --no-cache --progress plain
