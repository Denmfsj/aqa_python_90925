
from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")

    #
    page.locator('#user-name').fill('standard_user', timeout=1000)  # login
    page.locator('#password').fill('secret_sauce', timeout=1000)  # password

    page.get_by_role('button').click(timeout=500)  # login button

    # елемент тільки на головній сторінці
    expect(page.locator('//span[@data-test="title"]')).to_have_text('Products', timeout=2000)
    page.wait_for_timeout(1000)
