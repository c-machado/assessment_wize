#!/usr/bin/env bash


printf "STARTING TEST:\n"

pytest tests/ -m "load-more-" --html=reports/blog/tag.html
#pytest tests/ -m "search" --html=reports/blog/search_ff.html
pytest tests/ -m "feed-article" --html=reports/blog/feed_ff.html
#pytest tests/ -m "header" --html=reports/blog/header_ff.html
#pytest tests/ -m "footer" --html=reports/blog/footer_ff.html &
#pytest tests/ -m "cookie" --html=reports/blog/cookie_ff.html
#pytest tests/ -m "newsletter" --html=reports/blog/newsletter_ff.html

#docker run --rm -v "$(pwd)"/reports:/chrome-test/tests/reports chrome/linux:latest


