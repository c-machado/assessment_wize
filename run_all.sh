#!/usr/bin/env bash


printf "STARTING TESTS BUSINESS CRITICAL:\n"

#pytest tests/ -m "header_business_critical" --html=reports/blog/business_critical_header.html # BEI

#pytest tests/ -m "search_nav_business_critical" --html=reports/blog/business_critical_search_nav.html # GABO

# If the videos tests fails please try to them without headless mode
#pytest tests/ -m "videos" --html=reports/blog/article-videos.html # BEI

#pytest tests/ -m "standalone_newsletter" --html=reports/blog/business_critical_standalone_newsletter.html # BEI
#pytest tests/ -m "toast_standalone_newsletter" --html=reports/blog/business_critical_toast_standalone_newsletter.html # BEI
#pytest tests/ -m "homepage_newsletter" --html=reports/blog/business_critical_homepage_newsletter.html # BEI

#pytest tests/ -m "footer_business_critical" --html=reports/blog/business_critical_footer.html #BEI

#pytest tests/ -m "cookie" --html=reports/blog/business_critical_cookie.html

#pytest tests/ -m "article-related" --html=reports/blog/article-related-lf.html
#pytest tests/ -m "article-date-format-related-stories" --html=reports/blog/article-related-date-lf.html

#printf "STARTING TESTS REGRESSION:\n"

#pytest tests/ -m "header_regression" --html=reports/blog/regression_header.html
#pytest tests/ -m "search_regression" --html=reports/blog/regression_search.html
#pytest tests/ -m "footer_regression" --html=reports/blog/footer_regression.html





#pytest tests/ -m "search" --html=reports/blog/search-global.html
#pytest tests/ -m "search-home" --html=reports/blog/search-home.html
#pytest tests/ -m "search-category" --html=reports/blog/search-cat.html
#pytest tests/ -m "search-subcategory" --html=reports/blog/search-subcat.html
###pytest tests/ -m "search-article" --html=reports/blog/article-search.html
#pytest tests/ -m "search-sitespace" --html=reports/blog/search-sitespace.html

#pytest tests/ -m "feed-article-load-more" --html=reports/blog/feed-load-more.html
#pytest tests/ -m "feed-article-tagging" --html=reports/blog/feed-tagging.html
#pytest tests/ -m "feed-article-date-format" --html=reports/blog/feed-date-format.html
#

#pytest tests/ -m "article-inline" --html=reports/blog/article-inline-.html

#
#pytest tests/ -m "press" --html=reports/blog/press.html
#pytest tests/ -m "redirects" --html=reports/blog/redirects.html

