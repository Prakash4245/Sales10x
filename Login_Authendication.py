from playwright.sync_api import Page

def login(page: Page, username: str, password: str):
    # Locate the username and password textboxes and type the credentials
    username_txtbox = page.locator('input[name="username"]')
    username_txtbox.fill(username)

    password_txtbox = page.locator('input[name="password"]')
    password_txtbox.fill(password)

    # Locate and click the login button
    button_selector = 'button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeSmall.MuiButton-containedSizeSmall.MuiButton-colorPrimary.MuiButton-fullWidth.css-194qkv'
    page.locator(button_selector).click()

    # Wait for some time to allow the login process to complete
    page.wait_for_timeout(3000)
