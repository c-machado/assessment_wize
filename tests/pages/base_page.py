from w3lib.url import url_query_parameter

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators


class BasePage(object):

    # It takes in the browser, which will be passed in from the test case
    def __init__(self, browser):
        # Set my local self.browser variable to be whatever browser it's passed in
        self.browser = browser

    def click_tab(self, tab_locator):
        self.browser.click_to_element(tab_locator)

###########
    @staticmethod
    def get_ap_parameter(platform, channel):
        for platform_id, app_parameter in Constants.AP_WIN_PARAMETER.items():
            if channel != 'canary':
                if channel.upper() + platform == platform_id:
                    print('app_parameter no canary: ', app_parameter)
                    return app_parameter
            elif channel == 'canary':
                if channel.upper() + platform == platform_id:
                    print('app_parameter en canary: ', app_parameter, 'channel', channel, 'platform_id', platform_id)
                    return app_parameter

    @staticmethod
    def get_browser_parameter(web_browser):
        for web_browser_value, web_browser_id in Constants.BROWSER_VERSION.items():
            if web_browser_value in web_browser:
                return web_browser_id

    @staticmethod
    def get_link_selector(link):
        for link_id, locator_link in PageLocators.link_locators.items():
            if link_id == link:
                print('locator ', locator_link, 'locator', locator_link)
                return locator_link

    @staticmethod
    def get_id_per_platform(desktop_versions):
        for platform, platform_id in PageLocators.platforms_labels_to_ids.items():
            if platform == desktop_versions:
                print('platform label to id ', platform_id)
                return platform_id

    @staticmethod
    def get_retry_locator_win_other_channel(chrome):
        if chrome.__contains__("beta") or chrome.__contains__("canary") or chrome.__contains__("dev"):
            return PageLocators.retry_link_other
        else:
            return PageLocators.retry_link_win

    @staticmethod
    def get_query_parameter(parameter, url):
        try:
            return url_query_parameter(url, parameter)
        except KeyError:
            return 'Key error'

    def get_status_redirect(self):
        return self.browser.execute_script("var xhr = new XMLHttpRequest();" 
                                           "xhr.open('GET', window.location, false);"
                                           "xhr.send(null);" "return xhr.status")

    # This will iterate on the locators according the platform parameter received and click the corresponding link
    @staticmethod
    def get_unsupported_message(channel):
        for channel_id, message in Constants.UNSUPPORTED_DOWNLOAD_MSG.items():
            if channel_id == channel:
                return message

    @staticmethod
    def switch_to_active_tab(browser):
        browser.switch_to.window(browser.window_handles[1])

    def update_eula_checkbox(self, checkbox_locator):
        self.browser.click_to_element(checkbox_locator)

    @staticmethod
    def validate_needs_admin(channel_downloaded, download_uri):
        if channel_downloaded != 'canary':
            assert download_uri.__contains__(Constants.NEEDS_ADMIN_PREFER)
        else:
            assert download_uri.__contains__(Constants.NEEDS_ADMIN_CANARY)

    def visibility_of_modal(self, modal):
        for modal_label, modal_id in Constants.EULA_MODAL.items():
            if modal_label == modal:
                print('visibility of chrome os modal ', self.browser.is_modal_visible_by_id(modal_id))
                return self.browser.is_modal_visible_by_id(modal_id)