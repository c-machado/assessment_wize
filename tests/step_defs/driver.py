import os
import time
import warnings

import selenium
# from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common import exceptions

from selenium.webdriver.safari.options import Options
from selenium.webdriver.safari.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from tests.consts.constants import Constants
from tests.step_defs.i_driver import IDriver

"""IComponent: Methods the component MUST implement" \
 it will derive from the abstract Driver class.
"""


class Driver(IDriver):

    def __init__(self):
        self.driver = None
        self.web_element = None

    def start(self, web_browser, viewport):
        if web_browser in Constants.UA_BROWSERS:
            self.build_driver_with_user_agent(web_browser, viewport)
        else:
            self.build_driver_for_local(web_browser, viewport)

    def build_driver_for_local(self, web_browser, viewport):
        if web_browser == "chrome":
            self.build_chrome_driver(ChromeDriverManager().install(), viewport)
        elif web_browser == 'firefox':
            self.build_firefox_driver(GeckoDriverManager().install(), viewport)
        elif web_browser == 'safari':
            self.build_safari_driver(viewport)
        elif web_browser == 'edge':
            self.build_edge_driver(viewport)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        return self.driver

    def build_driver_with_user_agent(self, web_browser, viewport):
        for browser_id, ua in Constants.USER_AGENTS.items():
            if browser_id == web_browser:
                if web_browser in Constants.UA_BROWSERS:
                    self.set_chrome_ua(ua, viewport)
                    print(ua)
                elif web_browser == 'firefox_ua':
                    self.set_firefox_ua(ua)
                warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
                return self.driver

    def build_chrome_driver(self, driver_path, viewport):
        print('build chrome')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": r"./tmp",
        })
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        size_viewport = self.get_window_size(viewport)
        options.add_argument(size_viewport)
        options.set_capability("acceptInsecureCerts", True)
        # options.add_argument('--start-maximized')
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--remote-debugging-port=9222")
        # chrome://inspect/#devices

        # path_chrome = r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
        # options.add_argument(r'--user-data-dir=/Users/machadoca/Library/Application\ Support/Google/Chrome')  # your chrome user data directory
        # options.add_argument(r'--profile-directory=/Users/machadoca/Library/Application Support/Google/Chrome/Default')  # the profile with the extensions loaded

        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s,
                                       options=options)
        # device_metrics = {"width": 600,
        #                   "height": 1000,
        #                   "mobile": True,
        #                   "deviceScaleFactor": 50
        #                   }
        # self.driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", device_metrics)

    def build_edge_driver(self, driver_path, viewport):
        options = Options()
        # options.add_argument('--headless')
        s = Service(driver_path)
        self.driver = webdriver.Edge(options=options)

    def build_firefox_driver(self, driver_path, viewport):
        options = Options()
        options.add_argument('--headless')
        width = self.get_win_width(viewport, Constants.FF_WINDOWS_WIDTH)
        height = self.get_win_height(viewport, Constants.FF_WINDOWS_HEIGHT)
        options.add_argument(width)
        options.add_argument(height)
        s = Service(driver_path)
        self.driver = webdriver.Firefox(service=s,
                                        options=options)

    # def build_ie_driver(self, web_browser):
    #     if web_browser == 'ie':
    #         caps = DesiredCapabilities.INTERNETEXPLORER
    #         caps['acceptSslCerts'] = False
    #         caps['javascriptEnabled'] = True
    #         # caps.update(self.driver)
    #         self.driver = webdriver.Ie(
    #             executable_path=
    #             "C:\\Users\\machadoca\\pyexecnetcache\\keyword\\tests\\bin\\windows\\IEDriverServer.exe",
    #             capabilities=caps)
    #         return self.driver

    # DeprecationWarning: port has been deprecated, please set it via the service class
    def build_safari_driver(self, viewport):
        options = Options()
        # options.set_capability('port', 0)
        # options.add_argument('acceptInsecureCerts=True')
        width = self.get_win_width(viewport, Constants.SAFARI_WINDOWS_WIDTH)
        height = self.get_win_height(viewport, Constants.SAFARI_WINDOWS_HEIGHT)
        # options.add_argument(width)
        # options.add_argument(height)
        self.driver = webdriver.Safari(options)
        # self.driver.set_window_size(width, height)

    # options, error with chrome running in parallel:
    # https://stackoverflow.com/questions/65418237/chromedriver-crashing-on-some-websites
    # def build_remote_driver(self, run_type, web_browser):
    #     url = "http://localhost:4444/wd/hub"
    #     browser = os.getenv('VERSION')
    #     print('config_browser', run_type)
    #     # # if browser == "chrome":
    #     if web_browser == "chrome":
    #         options = webdriver.ChromeOptions()
    #         # options.BinaryLocation = ChromeDriverManager().install()
    #         #     # options.set_capability("browserVersion", "67")
    #         #     # options.set_capability("platformName", "Windows XP")
    #         options.add_argument("--disable-dev-shm-usage")
    #         #     # caps.update(browser)
    #         caps = {'browserName': 'chrome'}
    #         self.driver = selenium.webdriver.Remote(
    #             command_executor=url,
    #             desired_capabilities=caps,
    #             options=options
    #         )
    #         return self.driver
    #     elif web_browser == "firefox":
    #         caps = {'browserName': 'firefox'}
    #         self.driver = selenium.webdriver.Remote(
    #             command_executor='http://localhost:4444/wd/hub',
    #             desired_capabilities=caps)
    #         return self.driver

    def set_chrome_ua(self, ua, viewport):
        self.build_chrome_driver(ChromeDriverManager().install(), viewport)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": ua})

    # selenium.common.exceptions.InvalidCookieDomainException: Message: invalid cookie domain
    def set_cookie(self):
        try:
            cookie_data = {
                "domain": "gweb-uniblog-publish-stage.appspot.com",
                "path": "/",
                "name": "GCP_IAAP_AUTH_TOKEN_B01769F84EF452A5",
                "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjkzNDFhYmM0MDkyYjZmYzAzOGU0MDNjOTEwMjJkZDNlNDQ1MzliNTYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyNjMzNTM0OTQ5MTYtYXR1NTRrM3YxOTQ5MXBnZnNqampqOTdjZWNjNG52bmIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyNjMzNTM0OTQ5MTYtYXR1NTRrM3YxOTQ5MXBnZnNqampqOTdjZWNjNG52bmIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDg1NTgwNDI2NDc1NDMyNDcxOTEiLCJoZCI6Imh1Z2VpbmMuY29tIiwiZW1haWwiOiJjbWFjaGFkb0BodWdlaW5jLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiTndDbGZhbW80MVhRcGRyQTV4eGdHdyIsImdvb2dsZSI6eyJnaWMiOiJBR09vNTJpdUxTMzVSb1FsVUM5d2dxbFV5ZXNHbm93UmxZbUtBVFVoN0puajd0NnhUQ21qb3FuMmNJeFJzLVNreU1sdTJreWdrdHlseFRQV05aajZOZWVMYVJZYi0tbEJwTVgwLU9pMlpxeE9qQy1hOE1oek1fOVg0NXNhbkp4WGUyWW1RcnpsQlRGeDBPa0xOTk1nX2VnaWJYNmJ3YnIzY05QLXk0RXZhT1o5X0ZCOWwyMnpNbHdnbFhjT3R3T2xPWDVZMll4SXZvSFZIUFdUbGZNcmVEU2F2V1BGMEk5RXl1ZDNrdyJ9LCJpYXQiOjE2Mzg4MTA1OTMsImV4cCI6MTYzODgxNDE5M30.fz-G5nOYbMJuFZxJCv0xR7iH5rDhpyTtMmtIe96ni4uFIHq275AkmP67Ick1gTGJlx5BBq6xewRTgNAHp0tbyx3rNl0jzgwHh2gT_nYFO9wLZ8WcRVrvyqCjNoRbBd94jxq2mWC1M90vt_OE7KBoHNuZRUFOam4k9xZxC73iBGPUy9G3RSMNop9cYB3arZjF4S-FVJRQGp8Ecv2eG0lxnNCOpjeas-iy8J5qunVUlX1MIIkLiRQS3coWuuJN00WN32BxoHWRg9UV7TquAUAY_62-UhYjhknI9uJhr4jHStmG81siwpl5VdwAjVX2MeS-rXNmSpYQcPCD_o69XY9a3Q",
                # "expirationDate": 1798790400,
                # "hostOnly": False,
                "httpOnly": True,
                "secure": False,
                # "session": False,
                "sameSite": "None"
            }
            self.driver.add_cookie(cookie_data)
            # self.driver.refresh()
        except exceptions.InvalidCookieDomainException as e:
            print(e)

    def set_firefox_ua(self, ua):
        self.build_firefox_driver(GeckoDriverManager().install())
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", ua)

    def refresh(self):
        self.driver.refresh()

    def add_cookie(self, cookie_data):
        self.driver.add_cookie(cookie_data)

    def get_cookie(self):
        self.driver.get_cookie()

    def driver_clear(self):
        self.driver.driver_clear()

    def current_url(self):
        return self.driver.current_url

    def click_to_element(self, clickable_element):
        self.wait_for_element_clickable(*clickable_element)
        self.wait_for_element_visible(*clickable_element)
        self.driver.find_element(*clickable_element).click()

    def close(self):
        self.driver.close()

    def __contains__(self, item):
        return self.driver.__contains__(item)

    def execute_script(self, script):
        return self.driver.execute_script(script)

    def execute_script_locator(self, script, locator):
        return self.driver.execute_script(script, locator)

    def find_element(self, *locator):
        self.wait_for_element_visible(*locator)
        if locator.__len__() == 2:
            return self.driver.find_element(*locator)
        return self.driver.find_element(*(locator[1], locator[2] % locator[0]))

    def find_elements(self, *locator):
        self.wait_for_element_visible(*locator)
        if locator.__len__() == 2:
            return self.driver.find_elements(*locator)
        return self.driver.find_elements(*(locator[1], locator[2] % locator[0]))

    def get_elements_list(self, locator):
        return self.driver.find_elements(*locator)

    def get_page_source(self):
        return self.driver.page_source

    def go_to_URL(self, url):
        self.driver.get(url)

    def go_back_to_url(self):
        self.driver.back()

    def get_select_options(self, locator):
        options = self.driver.find_element(*locator)
        return Select(options)

    def get_urls_list(self, locator):
        elements = self.driver.find_elements(*locator)
        urls = []
        for element in elements:
            urls.append(element.get_attribute("href"))
        return urls

    @staticmethod
    def get_window_size(viewport):
        for viewport_id, win_size in Constants.CHROME_WINDOWS_SIZE.items():
            if viewport_id == viewport:
                return win_size

    @staticmethod
    def get_win_width(viewport, width_browser):
        for viewport_id, width in width_browser.items():
            if viewport_id == viewport:
                return width

    @staticmethod
    def get_win_height(viewport, height_browser):
        for viewport_id, height in height_browser.items():
            if viewport_id == viewport:
                return height

    def maximize_window(self):
        self.driver.maximize_window()

    def move_to_element(self, to_element):
        from selenium.webdriver.common.action_chains import ActionChains
        action = ActionChains(self.driver)
        action.move_to_element(to_element).click().perform()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def switch_to_active_element(self, element):
        self.driver.switch_to.active_element(element)

    def switch_to_active_tab(self):
        handles_before = self.driver.window_handles
        print('tabs size', len(handles_before))
        wait = WebDriverWait(self.driver, 50)
        try:
            if handles_before == 1:
                wait.until(lambda x: len(handles_before) > 1)
        except Exception as e:
            print(e)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_page_load()

    def quit_browser(self):
        self.driver.quit()

    # TODO: Firefox explicitWait is not working properly
    def wait_for_page_load(self):
        wait = WebDriverWait(self.driver, 50)
        try:
            js_ready = self.execute_script("return document.readyState")
            wait.until(lambda x: js_ready == "complete")
        except Exception as e:
            print(e)

    def wait_for_feed_to_load(self, *locator):
        wait = WebDriverWait(self.driver, 50)
        try:
            length_list = len(self.driver.find_elements(*locator))
            print('length_list', length_list)
            wait.until(lambda x: length_list > 0)
        except Exception as e:
            print(e)

    def wait_for_element_clickable(self, *locator):
        wait = WebDriverWait(self.driver, 50)
        if locator.__len__() == 2:
            return wait.until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_element_visible(self, *locator):
        wait = WebDriverWait(self.driver, 50)
        if locator.__len__() == 2:
            return wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_not_visible(self, *locator):
        print('test')
        wait = WebDriverWait(self.driver, 50)
        if locator.__len__() == 2:
            print('test 2')
            return wait.until(expected_conditions.invisibility_of_element_located(locator))
