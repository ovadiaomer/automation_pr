import playwright.sync_api as p

PARAMS = [
    'x',
    'y'
]

url = "https://app.xyte.io/settings/groups?page=1"
def test_create_user(page: p.Page):
    # Navigate to the user management page
    page.goto(url)

    # Click the "Create User" button
    create_button = page.wait_for_selector("#create-user-button")
    create_button.click()

    # Fill out the user creation form
    username_input = page.wait_for_selector("#username-input")
    password_input = page.wait_for_selector("#password-input")
    username_input.type("testuser")
    password_input.type("testpassword")

    # Submit the form
    submit_button = page.wait_for_selector("#submit-button")
    submit_button.click()

    # Verify that the user was successfully created
    success_message = page.wait_for_selector("#success-message")
    assert success_message.inner_text == "User created successfully!"