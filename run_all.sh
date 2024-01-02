#!/usr/bin/env bash


printf "STARTING TESTS:\n"

pytest tests/ -m "wizeline" --html=reports/checkout.html


