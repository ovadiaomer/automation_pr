import logging
import random
from typing import Literal

from playwright.sync_api import Page, expect, Locator

from src.ui_tests.pages.base import BasePage


class SettingsPage(BasePage):

    def __init__(self, page: Page) -> None:
        BasePage.__init__(self, page)
        self.setting_table = page.locator('div[class^=mantine-ScrollArea-root] div[class^=mantine-Tooltip-root]')
        self.setting_table_entry: Locator = lambda entry="Groups": self.setting_table.locator(f'a:text-is("{entry}")')
        self.create_group_button = self.page.locator("span")
        self.groups = Groups(self.page)

    def navigate(self):
        self.select_settings("Settings")
        expect(self.setting_table).not_to_have_count(0)

    def choose_in_settings_table(self, setting_entry: Literal["Users", "Groups"]):
        self.setting_table_entry(setting_entry).click()
        expect(self.groups.create_group_button).to_be_visible()
        expect(self.groups.group_table).to_be_visible()


class Groups:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.modal = self.page.locator(".modal-content")
        self.modal_input = self.modal.locator("input[name=name]")
        self.modal_submit = self.modal.locator("button[type=submit]")
        self.group_table = self.page.locator("div[role=rowgroup]")
        self.create_group_button = self.page.locator("span:text-is('Create Group')")
        self.row_by_text: Locator = lambda value: self.group_table.locator(f'div[role=row]', has=self.page.locator(
            f'div:text-is("{value}")'))

    def add_group(self, new_group_name: str = None) -> str:
        if new_group_name is None:
            new_group_name = f'automation_{random.randint(1, 999999)}'
        self.create_group_button.click()
        expect(self.modal).to_be_visible()
        self.modal_input.fill(new_group_name)
        self.modal_submit.click()
        expect(self.modal).not_to_be_visible()
        expect(self.row_by_text(value=new_group_name)).to_be_visible()
        return new_group_name

    def get_data_from_table(self, value):
        row = self.row_by_text(value)
        name = row.locator("div[id$=_name]").inner_text()
        member_count = row.locator("div[id$=_member_count]").inner_text()
        value_id = row.locator("div[id$=_id]").inner_text()
        return name, member_count, value_id
