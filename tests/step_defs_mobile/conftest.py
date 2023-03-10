import pytest


# print a message with the step in case of error
from pytest_bdd import parsers, given

from tests.consts.constants import Constants


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}', f'Scenario: {scenario}', f'Feature: {feature}')


# TODO: Firefox: ValueError: response body:
# {'message': "API rate limit exceeded for 186.155.54.112. (But here's the good news:
# Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
# 'documentation_url': 'https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting'}
# TODO: Safari initialization is not working with Selenium 4
# @pytest.fixture(params=["ios", "android"], scope="module", autouse=True)
@pytest.fixture(params=["ios"], scope="module", autouse=True)
def get_web_browser(request):
    return request.param


@pytest.fixture(params=["mobile"], scope="module", autouse=True)
def get_viewport(request):
    return request.param


