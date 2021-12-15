import pytest
from pytest_bdd import scenarios, given, when, then

from ..pages.locators import PageLocators
from ..consts.constants import Constants

scenarios("../features/")
# scenarios("../features/mac_platform/download_stable_mac.feature")
# scenarios("../features/linux_platform/linux_other_platforms.feature")
# scenarios("../features/windows_platform/download_stable_win.feature")

# BASE_URL = "https://www.google.com/"
BASE_URL = "https://chrome.sandbox.google.com/"


@given('a user is at the "<chrome>" website on "<platform>" and "<web_browser>"')
def at_the_chrome_page(chrome, platform, web_browser, browser):
    chrome_url = BASE_URL + chrome
    browser.start(platform, web_browser)
    browser.go_to_URL(chrome_url)
    print('current_url: ', browser.current_url())


@given('a user is at the "<chrome>" "<channel>" website on "<platform>" and "<web_browser>"')
def at_the_chrome_channel_page(browser, chrome, channel, platform, web_browser):
    chrome_url = BASE_URL + chrome + channel
    browser.start(platform, web_browser)
    browser.go_to_URL(chrome_url)


@given('a user is at the "<chrome>" "<page>" website on "<platform>" and "<web_browser>"')
def at_the_chrome_channel_page(browser, chrome, page, platform, web_browser):
    chrome_url = BASE_URL + chrome + page
    browser.start(platform, web_browser)
    browser.go_to_URL(chrome_url)


@given('a user is at the "<chrome>" website tagged with "<standalone>" parameter on "<platform>" and "<web_browser>"')
def at_the_chrome_channel_page(browser, chrome, standalone, platform, web_browser):
    chrome_url = BASE_URL + chrome + standalone
    browser.start(platform, web_browser)
    browser.go_to_URL(chrome_url)


@when('the user clicks on the Download button in the hero section')
# @pytest.mark.timeout(20)
def user_clicks_to_download_hero(browser):
    browser.click_to_element(PageLocators.download_cta_hero)


@when('the user chooses the "<installer>"')
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="TimeoutException")
def select_mac_version(home_page, installer):
    home_page.choose_installer_version(installer)


# TODO: remove the timeout / waitforelement(clickable or visible) / waitforJSReady are not working
@pytest.mark.timeout(10)
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="TimeoutException")
@then('the user is redirected to the "<chrome>" thank you page according to the "<platform>"')
def redirect_to_thank_you_page(browser, base_page, chrome, platform):
    # time.sleep(1)
    if platform.startswith("WIN"):
        browser.wait_retry(base_page.get_retry_locator_win_other_channel(chrome))
    else:
        browser.wait_retry(PageLocators.retry_link[platform[0:3].upper()])
    assert base_page.get_status_redirect() == 200
    assert Constants.THANK_YOU in browser.current_url()


# @pytest.mark.flaky(reruns=1, reruns_delay=0.5)
@then('the user is redirected to the "<chrome>" "<channel>" thank you page according to the "<platform>"')
def redirect_to_thank_you_page_other_platform(browser, base_page, chrome, channel, platform):
    # time.sleep(1)
    if platform.startswith("WIN"):
        browser.wait_retry(base_page.get_retry_locator_win_other_channel(channel))
    else:
        browser.wait_retry(PageLocators.retry_link[platform[0:3].upper()])
    assert base_page.get_status_redirect() == 200
    assert Constants.THANK_YOU in browser.current_url()


# |PARAMETER            | PLATFORM              | VALUE                      |
# |LANG                 | ALL                   | SAME                       |
# |APP_GUID             | ALL                   | SAME                       |
# |APP_NAME             | ALL                   | SAME                       |
# |NEEDS_ADMIN          | ALL                   | SAME                       |
@then('the system downloads Google Chrome on the selected "<channel>", "<platform>", "<web_browser>" and "<language>"')
def check_download_URI(browser, base_page, download_chrome, channel, platform, web_browser, language):
    browser.wait_untilJSReady()
    download_uri = browser.execute_script("return sessionStorage.getItem('downloadUri');")
    print('download uri: ', download_uri)
    direct_download_uri = browser.execute_script("return sessionStorage.getItem('directDownloadUri');")
    assert language == base_page.get_query_parameter(Constants.LANGUAGE_PARAM, download_uri)
    download_chrome.validate_download_uri(download_uri, direct_download_uri, web_browser, channel, platform)


@then('the system downloads the installer on the selected "<channel>", "<other_platform>",'
      ' "<web_browser>" and "<language>"')
def other_platform_check_download_uri(browser, download_chrome,  channel, other_platform, web_browser, language):
    download_uri = browser.execute_script("return sessionStorage.getItem('downloadUri');")
    print('download uri: ', download_uri)
    direct_download_uri = browser.execute_script("return sessionStorage.getItem('directDownloadUri');")
    download_chrome.validate_download_uri(download_uri, direct_download_uri, web_browser, channel, other_platform)


# |PARAMETER            | PLATFORM              | VALUE                |
# |STAGE_THANK_YOU      | ALL                   | THANK_YOU            |
@then('the system update the "<stage_ty>" to keep tracking of the regular workflow')
def validate_stage_thank_you_download_uri(browser, base_page, stage_ty):
    download_uri = browser.execute_script("return sessionStorage.getItem('downloadUri');")
    # After downloading, the user will get redirected to the Thank you page and the Installer script will ping
    # tools.google.com with the same parameters but the stage will be set to thank you.
    stage_in_url = base_page.get_query_parameter(Constants.STAGE_PARAM, download_uri)
    assert stage_in_url == Constants.STAGE_THANK_YOU


# |PARAMETER        | PLATFORM        | VALUE      |
# |STAGE_RETRY      | ALL             | RETRY      |
@then('the system update the "<stage_retry>" to keep tracking of the retry workflow')
def validate_stage_retry_download_uri(browser, base_page, stage_retry):
    # time.sleep(2)
    download_uri = browser.execute_script("return sessionStorage.getItem('downloadUri');")
    stage_in_url = base_page.get_query_parameter(Constants.STAGE_PARAM, download_uri)
    assert stage_in_url == Constants.STAGE_RETRY


@then('the user clicks on the Download again button according to "<platform>" and "<channel>"')
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5)
def click_retry_thank_you_page(browser, thank_you_page, platform, channel):
    # element = Constants.download_again
    # browser.execute_script("arguments[0].scrollIntoView(true);", element)
    # time.sleep(1)
    thank_you_page.click_to_retry_download_link(platform, channel)


# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="Cannot read properties of null (reading 'clientHeight')")
@given("the user scrolls down to the content")
def scroll_to_content(browser):
    # element = browser.execute_script("document.getElementById('js-download-now')")
    # browser.execute_script("arguments[0].scrollIntoView(true);", element)
    # browser.execute_script("window.scrollTo(0, document.getElementById('" +
    #                          Constants.FOOTER_ID + "').offsetTop - 80)")
    # browser.execute_script("window.resizeTo(1440,1080);")
    # browser.set_window_size("1440", "1220")
    # time.sleep(0.2)
    browser.set_window_size("1440", "1220")
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("window.scroll({top: document.body.scrollHeight-80, behavior: 'smooth'});")


@given("the user scrolls down to the other platforms link")
def scroll_to_download_section(browser):
    browser.set_window_size("1440", "1220")
    browser.execute_script("window.scroll({top: document.getElementById('js-other-platform'),"
                           " behavior: 'smooth'});")


@given("the user scrolls down to load the cta download in the nav menu")
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="TimeoutException")
def scroll_to_content(browser):
    browser.maximize_window()
    browser.execute_script("window.scroll({top: document.body.scrollHeight-80, behavior: 'smooth'});")


@given("the user scrolls down to the download section")
def scroll_to_download_section(browser):
    browser.set_window_size("1440", "1220")
    browser.execute_script("window.scroll({top: document.getElementsByClassName('chr-download-browser'),"
                           " behavior: 'smooth'});")


@when("the user clicks on the Download button in the main nav")
def user_clicks_download_nav(browser):
    browser.click_to_element(PageLocators.download_cta_nav)


@when("the system displays the download modal with ToS and the Additional ToS")
def links_tos_popup(browser):
    assert browser.is_element_visible(PageLocators.tos_link_popup).__contains__(Constants.TOS_LINK)
    assert browser.is_element_visible(PageLocators.additional_tos_popup).__contains__(Constants.ADD_TOS_LINK)


@when("the user clicks on the bottom button")
# @pytest.mark.flaky(reruns=1, reason="not clickable because another element <div class=' chr-header-v3__wrapper'> "
#                                     "obscures it. Sometimes, the nav bar is overlapping the modal")
def user_clicks_on_download_section(browser):
    browser.click_to_element(PageLocators.download_cta_bottom)


@when("the user clicks on the Other Platforms link")
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="Other element would receive the click:ga-event-label='chromebooks'")
def click_other_versions(browser):
    browser.click_to_element(PageLocators.other_platforms_link)


@when('the user chooses the OS "<desktop_version>"')
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="Other element would receive the click: "
#                                                       "<div class=' chr-footer-links__group'>")
def choose_desktop_os_version(browser, other_versions, desktop_version):
    other_versions.choose_os_desktop_version(desktop_version)


@then('the user clicks on the accept and install CTA according to "<desktop_version>"')
@pytest.mark.timeout(10)
def accept_install_desktop_version(browser, other_versions, desktop_version):
    other_versions.download_os_desktop_version(desktop_version)


@when('the user chooses the mobile "<os_version>"')
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="element not interactable:"
#                                                       " [object HTMLDivElement] has no size and location")
def choose_mobile_os_version(browser, other_versions, os_version):
    other_versions.choose_mobile_version(os_version)


@when('the user clicks on the accept and install CTA based on the "<platform>"')
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="TimeoutException")
def accept_install_download(home_page, platform):
    home_page.accept_installer_per_platform(platform)


# Comparison between the ga-label (because is the value that matches across locales) and the innerHtml to make
# this validation work across locales. Also, because this
# element is not visible True using is_displayed or visibility_of_element_located
# @pytest.mark.flaky(reruns=1, reruns_delay=0.5)
@given('the system displays a message informing the "<platform>" version is not supported in the current "<channel>"')
def visibility_unsupported_platform_msg(home_page, platform, channel):
    visible_message = home_page.is_deprecated_hero_visible(platform, channel)
    unsupported_expected_message = home_page.get_unsupported_message(channel)
    assert unsupported_expected_message in visible_message


@when('the user clicks on the link \'get Chrome Stable\' in the present "<platform>" and "<channel>"')
def user_clicks_to_get_stable(home_page, platform, channel):
    home_page.get_stable_version(platform, channel)


@then('the user is redirected to the stable version of the "<chrome>" footer')
def redirect_to_homepage(browser, chrome):
    home_url = BASE_URL + chrome
    print('url redirect: ', home_url)
    assert browser.current_url().__contains__(home_url)


@then('the system adds the "<install_data_index>" parameter to the download url')
def validate_install_data_index(browser, download_chrome, install_data_index):
    download_uri = browser.execute_script("return sessionStorage.getItem('downloadUri');")
    print('install_data_index', install_data_index)
    download_chrome.confirm_install_data_index(install_data_index, download_uri)
    # parameter = base_page.get_query_parameter(Constants.INSTALL_DATA_INDEX)
    # assert install_data_index == parameter


@when("the system displays the eula <modal>")
@when("the system displays the <modal>")
# @pytest.mark.flaky(rerun=1, reruns_delay=0.5, reason="element not interactable: [object HTMLDivElement] "
#                                                      "has no size and location")
def is_modal_visible(browser, base_page, modal):
    assert base_page.visibility_of_modal(modal)


# @then("the system displays the other versions <modal_supported>")
# def is_other_versions_visible(browser, base_page, modal_supported):
#     assert base_page.visibility_of_modal(modal_supported)


@when("the user clicks on the <link>")
def user_clicks_to_link(browser, base_page, link):
    element = base_page.get_link_selector(link)
    browser.click_to_element(element)


# @then("the user is redirected to the play store <url>")
# @then("the user is redirected to <url>")
# # @pytest.mark.execution_timeout(0.5)
# # @pytest.mark.teardown_timeout(0.4)
# def redirect_to_url(browser, url, base_page):
#     assert base_page.get_status_redirect() == 200
#     print('status base_page:', base_page.get_status_redirect())
#     print('url:', url)
#     print('current url:', browser.current_url())
#     assert browser.current_url().__contains__(url)
#
#
# @then("the user is redirected to the <url> in a new tab")
# # @pytest.mark.flaky(rerun=1, reruns_delay=0.5, reason="NetworkError: A network error occurred. Error 500,"
# #                                                      "IndexError: list index out of range")
# def redirect_to_url_new_tab(browser, base_page, url):
#     browser.switch_to_active_tab()
#     assert base_page.get_status_redirect() == 200
#     print('status base_page:', base_page.get_status_redirect())
#     print('url:', url)
#     print('current url:', browser.current_url())
#     assert browser.current_url().__contains__(url)


@when("the user clicks on Download")
def download_to_get_chrome_ios(browser):
    browser.click_to_element(PageLocators.download_cta_hero)
    # browser.get_text_alert()


@when("the user clicks on the checkbox to share reports and statistics")
def update_eula_checkbox(browser, base_page):
    checkbox = browser.find_element(*PageLocators.eula_help_checkbox)
    if checkbox.get_attribute('checked') == 'true':
        base_page.update_eula_checkbox(PageLocators.eula_help_checkbox)
    else:
        base_page.update_eula_checkbox(PageLocators.eula_help_checkbox)


@when("the user clicks on the checkbox to set chrome as default")
def update_eula_checkbox(browser, base_page):
    base_page.update_eula_checkbox(PageLocators.eula_default_checkbox)


@when("the page is loaded the analytics code is loaded")
def analytics_tag_loaded(browser):
    print("ga", browser.execute_script("return window.ga !== undefined"))
    assert browser.execute_script("return window.ga !== undefined")


@then('the system adds the analytics "<id_tracker>" tracker to the page')
def id_account_tracker(browser, id_tracker):
    page_tracker_id = browser.execute_script("return window.ga.getAll()[0].get('trackingId')")
    print('tracker id ', page_tracker_id)
    assert page_tracker_id == id_tracker
