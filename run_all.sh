#!/usr/bin/env bash


printf "STARTING MAC TEST:\n"

python -m pytest
#--html=reports/blog/home.html

#pytest tests/ -m "mac-env-other" --html=reports/mac/env-mac-other.html
#
#docker run --rm -v "$(pwd)"/reports:/chrome-test/tests/reports chrome/linux:latest
#
#printf "STARTING WIN TEST:\n"
#
#pytest tests/ -m "win-env" --html=reports/win/env-win.html
#
#pytest tests/ -m "win-env-other" --html=reports/win/env-win-other.html
#
#printf "STARTING CHROME OS TEST:\n"
#
#pytest tests/ -m "chromeos" --html=reports/chromeos/chromeos.html
#
#printf "STARTING ANDROID TEST:\n"
#
#pytest tests/ -m "android" --html=reports/android/android.html

