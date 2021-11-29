from abc import abstractmethod, ABCMeta


"""
    COMPONENT
    The base Component interface defines operations that can be altered by
    decorators.
    //defines the default actions
"""


class IDriver(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def start(self, platform, web_browser):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def go_to_URL(self, url):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def quit_browser(self):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def find_element(self, *locator):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def click_to_element(self, clickable_element):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def find_element_by_id(self, id):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def find_elements_by_tag_name(self, tag):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def current_url(self, url):
        raise NotImplementedError@staticmethod

    @staticmethod
    @abstractmethod
    def execute_script(self, url):
        raise NotImplementedError @ staticmethod

    @staticmethod
    @abstractmethod
    def __contains__(self, item):
        raise NotImplementedError @ staticmethod

    @staticmethod
    @abstractmethod
    def wait_untilJSReady(self):
        raise NotImplementedError @ staticmethod
