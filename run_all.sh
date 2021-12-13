#!/usr/bin/env bash


printf "STARTING TEST:\n"

#python -m pytest
#--html=reports/blog/home.html

pytest tests/ -m "keyword-test"
#--html=reports/blog/test.html

#docker run --rm -v "$(pwd)"/reports:/chrome-test/tests/reports chrome/linux:latest


