from tests.consts.constants import Constants
from tests.pages.base_page import BasePage


class DownloadChrome(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

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






