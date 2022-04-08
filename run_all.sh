#!/usr/bin/env bash


#printf "TESTS PASSED IN STAGE & PROD:\n"

#pytest tests/ -m "header-mobile" --html=reports/blog/header-mobile.html
#pytest tests/ -m "header" --html=reports/blog/header.html
#pytest tests/ -m "header-sitespace" --html=reports/blog/header-sitespace.html
#pytest tests/ -m "footer" --html=reports/blog/footer.html

pytest tests/ -m "search1" --html=reports/blog/search-global.html
#pytest tests/ -m "search-mobile" --html=reports/blog/search-migration-mobile.html
#pytest tests/ -m "search-home-mobile" --html=reports/blog/search-home.html
#pytest tests/ -m "search-category" --html=reports/blog/search-cat.html
#pytest tests/ -m "search-category-mobile" --html=reports/blog/search-cat-mobile.html
#pytest tests/ -m "search-subcategory-mobile" --html=reports/blog/search-subcat-mobile.html
#pytest tests/ -m "search-article" --html=reports/blog/article-search1.html
#pytest tests/ -m "search-article-mobile" --html=reports/blog/article-search-mobile.html
#pytest tests/ -m "search-sitespace" --html=reports/blog/search-sitespace.html
#pytest tests/ -m "search-sitespace-mobile" --html=reports/blog/search-sitespace-mobile.html

#pytest tests/ -m "feed-article-load-more" --html=reports/blog/feed-load-more.html
#pytest tests/ -m "feed-article-tagging" --html=reports/blog/feed-tagging.html
#pytest tests/ -m "feed-article-date-format" --html=reports/blog/feed-date-format.html

#printf "TESTS WITH ERRORS IN STAGE:\n"
#TODO: remove localStorage from the session before starting the tests
#pytest tests/ -m "cookie-mobile" --html=reports/blog/cookie-mobile.html
#pytest tests/ -m "newsletter1" --html=reports/blog/newsletter.html

#pytest tests/ -m "article" --html=reports/blog/article-videos.html
#pytest tests/ -m "article-inline" --html=reports/blog/article-inline.html
#pytest tests/ -m "article-related" --html=reports/blog/article-related.html
#pytest tests/ -m "article-date-format-related-stories" --html=reports/blog/article-related-date.html

#pytest tests/ -m "press" --html=reports/blog/press.html

#docker run --rm -v "$(pwd)"/reports:/chrome-test/tests/reports chrome/linux:latest


