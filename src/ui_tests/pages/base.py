from typing import Literal

from playwright.sync_api import Page, Locator


#This class is for generic page locators and functions
class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.side_bar = page.locator('.sidebar-nav')
        self.side_bar_entry: Locator = lambda entry="Settings": self.side_bar.locator(f'span:text-is("{entry}")')

    def select_settings(self, setting_entry: Literal["Devices", "Files", "Store", "Your Product", "Settings"]):
        self.side_bar_entry(setting_entry).click()