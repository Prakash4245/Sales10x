from playwright.sync_api import sync_playwright
from Login_Authendication import login

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()

    # Increase timeout to 60 seconds
    page.goto('http://54.86.161.144/', timeout=60000)
    page.wait_for_timeout(3000)

    # Call the login function from Login_Authendication
    login(page, 'superadmin@superadmin.com', '12345678')

    page.wait_for_timeout(3000)
    browser.close()
