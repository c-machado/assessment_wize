LATEST_FEED = {
    '/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=7&site_id=2&tags=&template=latestArticleItem',
    '/intl/de-de/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=7&site_id=8&tags=&template=latestArticleItem',
    '/intl/en-au/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=7&site_id=9&tags=&template=latestArticleItem',
    '/intl/en-in/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=7&site_id=10&tags=&template=latestArticleItem',
     '/perspectives/sundar-pichai/': '/api/v2/latest?author_ids=3453,41,1614,102,1402,399,150&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=7&site_id=2&tags=&template=latestArticleItem',
    '/outreach-initiatives/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=True&paginate=7&site_id=2&tags=accessibility,arts-and-culture,civics,digital-wellbeing,diversity-and-inclusion,education,entrepreneurs,google-news-initiative,googleorg,grow-with-google,nonprofits,public-policy,small-business,topics-student-programs,sustainability&template=latestArticleItem',
    '/technology/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=True&paginate=7&site_id=2&tags=ai,area-120,design,developers,families,health,next-billion-users,safety-and-security&template=latestArticleItem',
    '/intl/de-de/produkte/android-chrome-mehr/#android': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=True&paginate=7&site_id=8&tags=android&template=latestArticleItem',
    '/intl/en-in/products/platforms/#android': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=True&paginate=7&site_id=10&tags=android&template=latestArticleItem',
    '/intl/en-au/products/android-chrome-more/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=True&paginate=7&site_id=9&tags=google-pay,google-play&template=latestArticleItem',
    '/products/android/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=7&site_id=2&tags=android&template=latestArticleItem',
    '/inside-google/googlers/she-word/': '/api/v2/latest?author_ids=&category=article,perspective&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=5&site_id=2&tags=the-she-word&template=latestArticleItem',
    '/waze/': '/api/v2/latest?author_ids=&category=&date_start=&date_stop=&hero_template=heroArticleItem&is_main_hero=&paginate=7&site_id=2&tags=products-waze&template=latestArticleItem'
}

SEARCH_API = {
    '/': '/api/v2/search?paginate=12&order=relevance&site_id=2&query=text_to_search',
    '/intl/de-de/': '/api/v2/search?paginate=12&order=relevance&site_id=8&query=text_to_search',
    '/intl/en-au/': '/api/v2/search?paginate=12&order=relevance&site_id=9&query=text_to_search',
    '/intl/en-in/': '/api/v2/search?paginate=12&order=relevance&site_id=10&query=text_to_search'
}

SEARCH_SUGGESTIONS_API = {
    '/': '/api/v2/search-suggestions/?query=text_to_search&site_id=2&format=json',
    '/intl/de-de/': '/api/v2/search-suggestions/?query=text_to_search&site_id=8&format=json',
    '/intl/en-au/': '/api/v2/search-suggestions/?query=text_to_search&site_id=9&format=json',
    '/intl/en-in/': '/api/v2/search-suggestions/?query=text_to_search&site_id=10&format=json'
}

BASE_URI = 'https://blog.google/api/v2/latest?tags=android'
