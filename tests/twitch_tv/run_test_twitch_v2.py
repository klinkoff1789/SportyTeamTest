from logging import INFO

from logger import logger
from playwright.sync_api import sync_playwright

from data.urls import TwitchURL
from locators.media_locators import MOB_SEARCH_ICON, MOB_SEARCH_FIELD, SEARCH_TXT
from twich_base_test import TwitchPopupManager, TwitchPageActions


def run_test():
    with sync_playwright() as p:
        # 1. Setup Mobile Context (CRITICAL for m.twitch.tv)
        device = p.devices['Pixel 7']
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**device)
        page = context.new_page()

        # 2. Initialize the Framework Components
        popup_manager = TwitchPopupManager(page)
        popup_manager.register_all_handlers()
        actions = TwitchPageActions(page)

        # 3. Run the Test scenario
        logger.log(INFO, "Step 1: Open twitch_mobile_page")
        page.goto(TwitchURL)

        logger.log(INFO, "Step 1.1: Prep for Search icon to be visible")
        actions.get_clear_search()

        logger.log(INFO, "Step 2: Click on the search button")
        page.locator(MOB_SEARCH_ICON).click()

        logger.log(INFO, "Step 3: Input StarCraft II")
        page.locator(MOB_SEARCH_FIELD).type(SEARCH_TXT, delay=400)

        logger.log(INFO, "Step 4-5: Scroll down two times & Select one streamer")
        page.locator(MOB_SEARCH_FIELD).hover()
        actions.mob_scroll_down(element=2)

        logger.log(INFO, "Step 6: On the streamer page wait until all is loaded and take a screenshot")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="run_test_twitch_v2.png")

        # Teardown
        browser.close()


if __name__ == "__main__":
    run_test()
