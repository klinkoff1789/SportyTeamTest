import re

from playwright.sync_api import Page, expect
link = "https://www.twitch.tv/"

def test_web_app(page: Page):
    page.goto(link)
    expect(page).to_have_title(re.compile("Twitch"))
    popup_accept = page.locator("//button[contains(@class,'ScCoreButton-sc-ocjdkq-0') and contains(@class, 'cAajJv')]").first
    try:
        # page.expect_popup()
        expect(popup_accept).to_be_visible()
        print("Cookies popup is visible")
        popup_accept.click()
        print("Cookies popup clicked with Accepted")

    except Exception as e:
        print("Cookies popup was not shown", e)

    mob_search_icon = page.locator('//*[name()="path" and contains(@d, "M2 10.5a8.5 8.5 0 1 1 15.176")]')
    mob_search_icon.click()
    search_field = page.locator('//*/input["Search"]')
    search_field.type("StarCraft II", delay=400)
    search_field.hover()
    for i in range(1,3):
        page.mouse.down()
        print(f"scrolling down the {i} time")
        if i == 2:
            # time.sleep(10)
            page.locator(f'//*//li[2]/a//p[contains(@title, "StarCraft II")]').click(force=True)
    # on the streamer page wait until all is load and take a screenshot
    page.wait_for_load_state("networkidle")
    page.screenshot(path="screenshot.png")

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto('https://www.twitch.tv/')
#     userAgentSelector = "div.user-agent"
#     elementHandle = page.query_selector(userAgentSelector)
#     text = page.locator("h1").text_content()
#     print(text)
#     browser.close()