#!/usr/bin/env bash


printf "STARTING TEST:\n"

pytest tests/ -m "header" --html=reports/blog/header.html --self-contained-html
pytest tests/ -m "footer" --html=reports/blog/footer.html --self-contained-html

#docker run --rm -v "$(pwd)"/reports:/chrome-test/tests/reports chrome/linux:latest


