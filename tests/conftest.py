# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import os
import pytest

from playwright.sync_api import Playwright, Page

from src.ui_tests.pages.login import LoginPage
from src.ui_tests.pages.settings import SettingsPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def settings_page(page: Page) -> SettingsPage:
    return SettingsPage(page)


# Environment variables

def _get_env_var(varname: str) -> str:
    value = os.getenv(varname)
    assert value, f'{varname} is not set'
    return value


@pytest.fixture(scope='session')
def xyte_url() -> str:
    return "https://app.xyte.io/auth/sign-in"


@pytest.fixture(scope='session')
def get_url() -> str:
    return _get_env_var('URL')

@pytest.fixture(scope='session')
def get_user_for_login() -> str:
    return _get_env_var('USER')

@pytest.fixture(scope='session')
def get_password_for_login() -> str:
    return _get_env_var('PASSWORD')


# Request context

@pytest.fixture(scope='session')
def url(
    playwright: Playwright,
    xyte_url: str):

    return xyte_url
