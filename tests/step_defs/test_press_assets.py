from pytest_bdd import given, parsers, scenarios, then, when

scenarios('../features/press/press_filters.feature')


@when(parsers.parse('the user sets filter by type {type_filter}'))
def user_filter_by_type(press, type_filter):
    press.get_results_filter_by_type(type_filter)


@when(parsers.parse('the user sets filter by product {product_filter}'))
def user_filter_by_product(press, product_filter):
    press.get_results_filter_by_product(product_filter)


@when(parsers.parse('the user sets filter by topic {topic_filter}'))
def user_filter_by_topic(press, topic_filter):
    press.get_results_filter_by_topic(topic_filter)


@when(
    parsers.parse(
        'the user chooses the {filter_by_type} and {filter_by_product}'
    )
)
def user_filter_by_type_product(press, filter_by_type, filter_by_product):
    press.get_results_filter_by_type_and_product(
        filter_by_type, filter_by_product
    )


@then(
    parsers.parse('the system updates the grid with {type_filter} in {keyword}')
)
def assets_get_filtered_by_type(press, type_filter, keyword):
    actual_titles = press.get_titles_in_press_assets_page()
    print('actual_titles', actual_titles)
    api_url = press.get_api_url_with_type(type_filter, keyword)
    expected_titles = press.get_titles_in_press_asset_api(api_url)
    print('expected_titles', expected_titles)
    download_urls = press.get_assets_download_urls_per_filter_in_press_api(
        api_url
    )
    assert expected_titles == actual_titles
    assert press.confirm_download_url_per_assets(download_urls)


@then(
    parsers.parse(
        'the system shows the grid with the {type_filter} and {tag_filter} in {keyword}'
    )
)
def assets_get_filtered_by_type_and_tag(
    press, type_filter, tag_filter, keyword
):
    actual_titles = press.get_titles_in_press_assets_page()
    print('actual_titles', actual_titles)
    api_url = press.get_api_url_with_type_and_tag(
        type_filter, tag_filter, keyword
    )
    expected_titles = press.get_titles_in_press_asset_api(api_url)
    print('expected_titles', expected_titles)
    download_urls = press.get_assets_download_urls_per_filter_in_press_api(
        api_url
    )
    assert expected_titles == actual_titles
    assert press.confirm_download_url_per_assets(download_urls)
