#!/usr/bin/env bash


printf "STARTING TESTS BUSINESS CRITICAL:\n"

##ANI
#pytest tests/ -m "header_business_critical" --html=reports/blog/business_critical_header.html
#pytest tests/ -m "standalone_newsletter" --html=reports/blog/business_critical_standalone_newsletter.html #r
#pytest tests/ -m "homepage_newsletter" --html=reports/blog/business_critical_homepage_newsletter.html

#This tag needs to be run in Blog.google, not in publish-prod
#pytest tests/ -m "toast_standalone_newsletter" --html=reports/blog/business_critical_toast_standalone_newsletter.html

#pytest tests/ -m "cookie" --html=reports/blog/business_critical_cookie.html #R
#pytest tests/ -m "footer_business_critical" --html=reports/blog/business_critical_footer.html
#pytest tests/ -m "press" --html=reports/blog/press.html

#pytest tests/ -m "feed-article-load-more" --html=reports/blog/feed-load-more.html #r
#pytest tests/ -m "feed-article-tagging" --html=reports/blog/feed-tagging.html #r
pytest tests/ -m "feed-article-date-format2" --html=reports/blog/feed-date-format.html #r


## If the videos tests fail please try them without headless mode
#pytest tests/ -m "videos" --html=reports/blog/business_critical_article-videos.html
pytest tests/ -m "article-related2" --html=reports/blog/business_critical_article-related.html

#
##DAVE
#pytest tests/ -m "search_nav_business_critical" --html=reports/blog/business_critical_search_nav.html #url_africa

#pytest tests/ -m "search_suggestions_business_critical" --html=reports/blog/business_critical_search_suggestions.html
#pytest tests/ -m "search_suggestions_special_char_business_critical" --html=reports/blog/business_critical_search_suggestions_special_char.html
#pytest tests/ -m "search_results_page_business_critical" --html=reports/blog/business_critical_search_results_page.html
#pytest tests/ -m "search_results_page_special_char_business_critical" --html=reports/blog/business_critical_search_results_page_special_char.html

#printf "STARTING TESTS REGRESSION:\n"

#pytest tests/ -m "header-regression" --html=reports/blog/regression_header.html
#pytest tests/ -m "footer_regression" --html=reports/blog/regression_footer.html



#pytest tests/ -m "search_suggestions_regression" --html=reports/blog/regression_search_suggestions.html
#pytest tests/ -m "search_suggestions_special_char_regression" --html=reports/blog/regression_search_suggestions_special_char.html
#pytest tests/ -m "search_results_page_regression" --html=reports/blog/regression_search_results_page.html
#pytest tests/ -m "search_results_page_special_char_regression" --html=reports/blog/regression_search_results_page_special_char.html
#pytest tests/ -m "search_no_results_regression" --html=reports/blog/regression_search_no_results.html

##This tag needs to be run in Blog.google, not in publish-prod
#pytest tests/ -m "search_article_progress_bar" --html=reports/blog/regression_search_article_progress_bar.html
#pytest tests/ -m "article-inline" --html=reports/blog/regression_article-inline.html


##pytest tests/ -m "redirects" --html=reports/blog/redirects.html # IN PROGRESS

