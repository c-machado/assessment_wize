#!/usr/bin/env bash


printf "STARTING TEST:\n"

pytest tests/ -m "feed-article" --html=reports/blog/feed.html
#pytest tests/ -m "search-home" --html=reports/blog/search.html
#pytest tests/ -m "header-auth" --html=reports/blog/header.html
#pytest tests/ -m "footer" --html=reports/blog/footer.html
#pytest tests/ -m "cookie" --html=reports/blog/cookie.html
#pytest tests/ -m "newsletter" --html=reports/blog/newsletter.html

#docker run --rm -v "$(pwd)"/reports:/chrome-test/tests/reports chrome/linux:latest


