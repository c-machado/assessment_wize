#!/usr/bin/env bash

printf "STARTING DOCKER TEST:\n"

#python -m pytest -m "linux-env" --html=reports/linux/env-linux.html

python -m pytest -m "linux-env-other" --html=reports/linux/env-linux-other.html

