import os
import time
import warnings

import selenium
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager
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

    def start(self, platform, web_browser, viewport):
        if platform in Constants.PLATFORMS_WITH_UA:
            self.build_driver_with_user_agent(platform, web_browser, viewport)
        elif platform == Constants.PLATFORM_MAC:
            self.build_driver_for_local(web_browser, viewport)
        # elif platform == 'WIN10':
        #     self.build_ie_driver(platform, web_browser)
        else:
            raise Exception(f'"{platform}" is not supported')


    def build_driver_for_local(self, web_browser, viewport):
        if web_browser == "chrome":
            self.build_chrome_driver(ChromeDriverManager().install(), viewport)
        elif web_browser == 'firefox':
            self.build_firefox_driver(GeckoDriverManager().install(), viewport)
        elif web_browser == 'safari':

            self.driver = webdriver.Safari()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        return self.driver

    def build_driver_with_user_agent(self, platform, web_browser, viewport):
        for platform_id, ua in Constants.USER_AGENTS.items():
            if platform_id == platform and platform in Constants.PLATFORMS_WITH_UA:
                if web_browser in Constants.UA_BROWSERS:
                    self.set_chrome_ua(ua, viewport)
                elif web_browser == 'firefox':
                    self.set_firefox_ua(ua)
                warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
                return self.driver

    def set_chrome_ua(self, ua, viewport):
        self.build_chrome_driver(ChromeDriverManager().install(), viewport)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": ua})

    def set_firefox_ua(self, ua):
        self.build_firefox_driver(GeckoDriverManager().install())
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", ua)

    def build_firefox_driver(self, driver_path, viewport):
        options = Options()
        # options.add_argument('--headless')
        print('viewport firefox', viewport)
        if viewport == 'mobile':
            options.add_argument("--width="+ Constants.MOBILE_WIDTH)
            options.add_argument("--height="+ Constants.MOBILE_HEIGHT)
        elif viewport == 'tablet':
            options.add_argument("--width="+ Constants.TABLET_WIDTH)
            options.add_argument("--height="+ Constants.TABLET_HEIGHT)
        elif viewport == 'desktop':
            options.add_argument("--width="+ Constants.DESKTOP_WIDTH)
            options.add_argument("--height="+ Constants.DESKTOP_HEIGHT)
        self.driver = webdriver.Firefox(
            executable_path=driver_path,
            options=options
        )
        # self.driver.set_window_size(480,340)
        # set_viewport = self.get_ff_window_size(viewport)
        # print(set_viewport)
        # self.driver.set_window_size(set_viewport)


    def driver_clear(self):
        self.driver.driver_clear()

    def build_chrome_driver(self, driver_path, viewport):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": r"./tmp",
        })
        size_viewport = self.get_window_size(viewport)
        options.add_argument(size_viewport)
        # options.add_argument('--start-maximized')
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--remote-debugging-port=9222")
        # chrome://inspect/#devices
        self.driver = webdriver.Chrome(
            executable_path=driver_path,
            options=options
        )

    def build_ie_driver(self, web_browser):
        if web_browser == 'ie':
            caps = DesiredCapabilities.INTERNETEXPLORER
            caps['acceptSslCerts'] = False
            caps['javascriptEnabled'] = True
            # caps.update(self.driver)
            self.driver = webdriver.Ie(
                executable_path=
                "C:\\Users\\machadoca\\pyexecnetcache\\keyword\\tests\\bin\\windows\\IEDriverServer.exe",
                capabilities=caps)
            return self.driver

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    @staticmethod
    def get_window_size(viewport):
        for viewport_id, win_size in Constants.WINDOWS_SIZE.items():
            if viewport_id == viewport:
                return win_size

    @staticmethod
    def get_ff_window_size(viewport):
        for viewport_id, win_size in Constants.FF_WINDOWS_SIZE.items():
            if viewport_id.startswith(viewport):
                print('win_ff_size', win_size)
                return win_size


    def maximize_window(self):
        self.driver.maximize_window()

    # options, error with chrome running in parallel:
    # https://stackoverflow.com/questions/65418237/chromedriver-crashing-on-some-websites
    def build_remote_driver(self, run_type, web_browser):
        url = "http://localhost:4444/wd/hub"
        browser = os.getenv('VERSION')
        print('config_browser', run_type)
        # # if browser == "chrome":
        if web_browser == "chrome":
            options = webdriver.ChromeOptions()
            # options.BinaryLocation = ChromeDriverManager().install()
        #     # options.set_capability("browserVersion", "67")
        #     # options.set_capability("platformName", "Windows XP")
            options.add_argument("--disable-dev-shm-usage")
        #     # caps.update(browser)
            caps = {'browserName': 'chrome'}
            self.driver = selenium.webdriver.Remote(
                command_executor=url,
                desired_capabilities=caps,
                options=options
            )
            return self.driver
        elif web_browser == "firefox":
            caps = {'browserName': 'firefox'}
            self.driver = selenium.webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=caps)
            return self.driver

    def current_url(self):
        return self.driver.current_url

    def click_to_element(self, clickable_element):
        self.wait_for_element_clickable(*clickable_element)
        self.wait_for_element_visible(*clickable_element)
        self.driver.find_element(*clickable_element).click()

    def click_to_element_async(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def __contains__(self, item):
        return self.driver.__contains__(item)

    def execute_script(self, script):
        return self.driver.execute_script(script)

    def find_element(self, *locator):
        if locator.__len__() == 2:
            return self.driver.find_element(*locator)
        return self.driver.find_element(*(locator[1], locator[2] % locator[0]))

    def find_element_by_id(self, locator):
        self.driver.find_element_by_id(locator)

    def get_elements_in_modal(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_id(element)).perform()
        elements_list = self.driver.find_element_by_id(element)
        return elements_list.find_elements_by_tag_name("a")

    def find_element_by_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath)

    def find_element_by_css_selector(self, css):
        self.driver.find_element_by_css_selector(css)

    def find_elements_by_tag_name(self, tag):
        self.driver.find_elements_by_tag_name(tag)

    def go_to_URL(self, url):
        self.driver.get(url)

    def is_element_visible(self, element):
        visible_element = self.driver.find_element(*element)
        return visible_element.get_attribute("href")

    def is_modal_visible_by_id(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_id(element)).perform()
        return self.driver.find_element_by_id(element).is_displayed()

    def is_displayed(self):
        self.driver.is_displayed()

    def get_inner_html(self, element):
        element = self.driver.find_element(*element)
        return element.get_attribute('innerHTML')

    def match_current_url(self, url):
        return self.driver.current_url.__contains__(url)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def switch_to_active_tab(self):
        handles_before = self.driver.window_handles
        wait = WebDriverWait(self.driver, 50)
        wait.until(lambda x: len(handles_before) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def accept_alert(self):
        self.driver.switch_to().alert().accept()

    def get_text_alert(self):
        self.driver.switch_to.alert.accept()

    def implicitly_wait(self, wait_time):
        self.driver.implicitly_wait(wait_time)

    def wait_untilJSReady(self):
        wait = WebDriverWait(self.driver, 2000)
        try:
            js_ready = self.execute_script("return document.readyState")
            if js_ready == "complete":
                print(js_ready)
                wait.until(lambda x: self.driver.execute_script("return document.readyState") == "complete")
        except Exception as e:
            print(e)

    def wait_retry(self, locator):
        self.wait_for_element_clickable(*locator)
        self.wait_for_element_visible(*locator)

    def wait_for_element_clickable(self, *locator):
        wait = WebDriverWait(self.driver, 50)
        if locator.__len__() == 2:
            return wait.until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_element_visible(self, *locator):
        wait = WebDriverWait(self.driver, 50)
        if locator.__len__() == 2:
            return wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_not_visible(self, *locator):
        wait = WebDriverWait(self.driver, 50)
        if locator.__len__() == 2:
            return wait.until(expected_conditions.invisibility_of_element_located(locator))