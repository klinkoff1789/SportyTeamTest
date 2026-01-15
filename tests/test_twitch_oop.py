from logging import INFO

from logger import logger
from playwright.sync_api import Page, expect

from locators.media_locators import MOB_SEARCH_SECOND_DROPDOWN
from pages.twitch_mobile_page import TwitchMobilePage


def accept_cookies_popup2(_page):
    try:
        expect(_page.cookies_popup).to_be_visible()
        logger.log(INFO, "Cookies popup is visible")
        _page.cookies_popup.click()
        logger.log(INFO, "Cookies popup clicked with Accepted")

    except Exception as e:
        logger.log(INFO, "Cookies popup was not shown", e)

def mob_scroll_down2(_page, element=2):
    """
    :param _page:
    :param element: element is an integer start with 2,
    scroll down to the element in dropdown search results
    (defaults to 2)
    """
    for i in range(1, element + 1):
        _page.mouse.down()
        print(f"Scrolling down the {i} time")
        if i == element:
            select_locator = _page.locator(MOB_SEARCH_SECOND_DROPDOWN.format(element))
            try:
                select_locator.click()
            except Exception as e:
                print(e)


def test_twitch_mob(page: Page):
    tw_page = TwitchMobilePage(page)
    logger.log(INFO, "Step 1: Open twitch_mobile_page")
    tw_page.open()

    logger.log(INFO, "Step 1.1: Accept cookies popup")
    accept_cookies_popup2(tw_page)
    # accept_cookies_popup(tw_page)

    logger.log(INFO, "Step 2: Click on the search button")
    tw_page.mob_search_icon.click()

    logger.log(INFO, "Step 3: Input StarCraft II")
    tw_page.mob_search_field.type("StarCraft II", delay=400)

    logger.log(INFO, "Step 4-5: Scroll down two times & Select one streamer")
    tw_page.mob_search_field.hover()
    mob_scroll_down2(tw_page, element=2)
    # mob_scroll_down(tw_page, element=2)

    logger.log(INFO, "Step 6: On the streamertw_page wait until all is loaded and take a screenshot")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="scr_twitch_oop.png")
