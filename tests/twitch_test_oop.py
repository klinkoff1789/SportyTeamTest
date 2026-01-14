from logging import INFO

from logger import logger

from twitch_base_test import TwitchBaseTest


class TwitchMobilePageTest(TwitchBaseTest):
    def before(self, browser):
        self.pages = browser.new_page()

    #TODO add new implementation with OOP(incomplete)
    def test_mob_page(self):

        page = self.pages.twitch_mobile_page
        logger.log(INFO, "Step 1: Open twitch_mobile_page")
        page.open()

        logger.log(INFO, "Step 1.1: Accept cookies popup")
        page.accept_cookies_popup()

        logger.log(INFO, "Step 2: Click on the search button")
        page.mob_search_icon().click()

        logger.log(INFO, "Step 3: Input StarCraft II")
        page.mob_search_field().type("StarCraft II", delay=400)

        logger.log(INFO, "Step 4-5: Scroll down two times & Select one streamer")
        page.mob_search_field().hover()
        page.mob_scroll_down(element=2)

        logger.log(INFO, "Step 6: On the streamer page wait until all is loaded and take a screenshot")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="screenshot.png")

