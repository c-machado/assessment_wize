#!/usr/bin/env bash


printf "STARTING TESTS BUSINESS CRITICAL:\n"
#
#pytest tests/ -m "header_business_critical" --html=reports/blog/business_critical_header.html


#pytest tests/ -m "standalone_newsletter" --html=reports/blog/business_critical_standalone_newsletter.html
#pytest tests/ -m "homepage_newsletter" --html=reports/blog/business_critical_homepage_newsletter.html


#pytest tests/ -m "toast_standalone_newsletter" --html=reports/blog/business_critical_toast_standalone_newsletter.html
#pytest tests/ -m "cookie" --html=reports/blog/business_critical_cookie.html
#pytest tests/ -m "footer_business_critical" --html=reports/blog/business_critical_footer.html
#pytest tests/ -m "press" --html=reports/blog/press.html

#pytest tests/ -m "feed-article-load-more" --html=reports/blog/feed-load-more.html
#pytest tests/ -m "feed-article-tagging" --html=reports/blog/feed-tagging.html
#pytest tests/ -m "feed-article-date-format" --html=reports/blog/feed-date-format.html




# If the videos tests fail please try them without headless mode
#pytest tests/ -m "videos" --html=reports/blog/business_critical_article-videos.html
#pytest tests/ -m "article-related" --html=reports/blog/business_critical_article-related.html

#########

#pytest tests/ -m "search_nav_business_critical" --html=reports/blog/business_critical_search_nav.html


#pytest tests/ -m "search_suggestions_business_critical" --html=reports/blog/business_critical_search_suggestions.html # GABO
#pytest tests/ -m "search_suggestions_special_char_business_critical" --html=reports/blog/business_critical_search_suggestions_special_char.html # GABO
#pytest tests/ -m "search_results_page_business_critical" --html=reports/blog/business_critical_search_results_page.html # GABO
#pytest tests/ -m "search_results_page_special_char_business_critical" --html=reports/blog/business_critical_search_results_page_special_char.html # GABO



#printf "STARTING TESTS REGRESSION:\n"

#pytest tests/ -m "header-regression" --html=reports/blog/regression_header.html
#pytest tests/ -m "footer_regression" --html=reports/blog/regression_footer.html

#pytest tests/ -m "article-inline" --html=reports/blog/regression_article-inline.html
#########

###/ok-(doesn't exist)-pytest tests/ -m "search_regression" --html=reports/blog/regression_search.html # GABO


#pytest tests/ -m "search_suggestions_regression" --html=reports/blog/regression_search_suggestions.html # GABO
#pytest tests/ -m "search_suggestions_special_char_regression" --html=reports/blog/regression_search_suggestions_special_char.html # GABO
#pytest tests/ -m "search_results_page_regression" --html=reports/blog/regression_search_results_page.html # GABO
#pytest tests/ -m "search_results_page_special_char_regression" --html=reports/blog/regression_search_results_page_special_char.html # GABO
#pytest tests/ -m "search_no_results_regression" --html=reports/blog/regression_search_no_results.html # GABO
#pytest tests/ -m "search_article_progress_bar" --html=reports/blog/regression_search_article_progress_bar.html # GABO


##pytest tests/ -m "redirects" --html=reports/blog/redirects.html # IN PROGRESS

