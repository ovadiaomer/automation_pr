
from playwright.sync_api import Page, expect

from src.ui_tests.pages.base import BasePage


class LoginPage(BasePage):
    url = "https://app.xyte.io/auth/sign-in" #TODO move out (should be inject os.environ currently set in conftest and can be pull as fixture)
    user = "Ovadia.omero@gmail.com" #TODO remove to conftest or os.environ
    password = "PWjh3Pn4Q5LAYyT"  #TODO remove secret

    def __init__(self, page: Page) -> None:
        BasePage.__init__(self, page)
        self.email_input = page.locator('input[name=email]')
        self.password_input = page.locator('input[name=password]')
        self.signin_button = page.locator('button[type=submit]')

    def navigate(self):
        self.page.goto(self.url)

    def is_loaded(self):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()

    def enter_credentials(self, user: str, password: str):
        self.email_input.fill(user)
        self.password_input.fill(password)

    def login(self, user: str, password: str):
        self.enter_credentials(user, password)
        expect(self.signin_button).to_be_enabled()
        self.signin_button.click()
        expect(self.side_bar).to_be_visible()
