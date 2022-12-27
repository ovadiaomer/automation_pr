import pytest
from playwright.sync_api import Page

from src.ui_tests.pages.login import LoginPage
from src.ui_tests.pages.settings import SettingsPage

#Can add the following decorator will require few minor changes in test
# @pytest.mark.parametrize("user, is_valid", [
#     ("valid@user.com", True),
#     ("valid@user.com", False),
#     (".com", False),
#     ("", False),
# ])

def test_xyte_add_group(
        page: Page,
        login_page: LoginPage, settings_page: SettingsPage, login) -> None:
    login
    settings_page.navigate()
    settings_page.choose_in_settings_table("Groups")
    new_group = settings_page.groups.add_group()
    name, member_count, value_id = settings_page.groups.get_data_from_table(new_group)
    assert name == new_group
    assert member_count == '1'
    assert value_id is not None
