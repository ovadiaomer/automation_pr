
from playwright.sync_api import Page
from typing import List


class ResultPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.element = page.locator('')

    def do_something(self):
        pass
