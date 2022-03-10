#!/usr/bin/env bash


printf "STARTING TEST:\n"

pytest tests/ -m "feed-article-load-more" --html=reports/blog/feed-load-more.html
pytest tests/ -m "feed-article-tagging" --html=reports/blog/feed-tagging.html
pytest tests/ -m "feed-article-date-format" --html=reports/blog/feed-date-format.html
pytest tests/ -m "search" --html=reports/blog/search.html
pytest tests/ -m "header" --html=reports/blog/header.html
pytest tests/ -m "footer" --html=reports/blog/footer.html
pytest tests/ -m "cookie" --html=reports/blog/cookie.html
pytest tests/ -m "newsletter" --html=reports/blog/newsletter.html

pytest tests/ -m "search-home" --html=reports/blog/search-home.html
pytest tests/ -m "search-subcategory" --html=reports/blog/search-subcat.html
pytest tests/ -m "search-category" --html=reports/blog/search-cat.html
pytest tests/ -m "search-article" --html=reports/blog/article-search.html
pytest tests/ -m "search" --html=reports/blog/search-migration.html

pytest tests/ -m "article" --html=reports/blog/article-videos.html
pytest tests/ -m "article-inline" --html=reports/blog/article-inline.html


#docker run --rm -v "$(pwd)"/reports:/chrome-test/tests/reports chrome/linux:latest


