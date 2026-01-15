import re
from logging import INFO
from logger import logger
from playwright.sync_api import Page, expect
link = "https://www.twitch.tv/"

def test_web_app(page: Page):
    logger.log(INFO, "\nStep 1: Open twitch_mobile_page")
    page.goto(link)
    expect(page).to_have_title(re.compile("Twitch"))

    logger.log(INFO, "Step 1.1: Accept cookies popup")
    popup_accept = page.locator("//button[contains(@class,'ScCoreButton-sc-ocjdkq-0') and contains(@class, 'cAajJv')]").first
    try:
        # page.expect_popup()
        expect(popup_accept).to_be_visible()
        print("Cookies popup is visible")
        popup_accept.click()
        print("Cookies popup clicked with Accepted")
    except Exception as e:
        print("Cookies popup was not shown", e)

    logger.log(INFO, "Step 2: Click on the search button")
    mob_search_icon = page.locator('//*[name()="path" and contains(@d, "M2 10.5a8.5 8.5 0 1 1 15.176")]')
    mob_search_icon.click()

    logger.log(INFO, "Step 3: Input StarCraft II")
    search_field = page.locator('//*/input["Search"]')
    search_field.type("StarCraft II", delay=400)

    logger.log(INFO, "Step 4-5: Scroll down two times & Select one streamer")
    search_field.hover()
    for i in range(1,3):
        page.mouse.down()
        print(f"Scrolling down: {i} time")
        if i == 2:
            # time.sleep(10)
            page.locator('//*//li[2]/a//p[contains(@title, "StarCraft II")]').click(force=True)

    logger.log(INFO, "Step 6: On the streamer page wait until all is loaded and take a screenshot")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="screenshot.png")
