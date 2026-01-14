from playwright.sync_api import Page, expect

# def test_web_app(page: Page):
#     page.goto("https://www.twitch.tv/")

def test_has_title(page: Page):
    # Navigate to the Playwright website
    page.goto("https://playwright.dev/")

    # Expect the page title to contain "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))