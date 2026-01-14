from playwright.sync_api import expect

from locators.media_locators import MOB_SEARCH_SECOND_DROPDOWN
from pages import twitch_mobile_page


class TwitchBaseTest:
    def __init__(self):
        self.page = twitch_mobile_page.TwitchMobilePage()

    def accept_cookies_popup(self):
        try:
            # page.expect_popup()
            expect(self.page.cookies_popup()).to_be_visible()
            print("Cookies popup is visible")
            self.page.cookies_popup().click()
            print("Cookies popup clicked with Accepted")

        except Exception as e:
            print("Cookies popup was not shown", e)

    def mob_scroll_down(self, element=2):
        """
        element is an integer start with 2
        :param element: scroll down to the element in dropdown search results
        (defaults to 2)
        """
        for i in range(1, element + 1):
            self.page.mouse.down()
            print(f"scrolling down the {i} time")
            if i == element:
                # time.sleep(10)
                try:
                    self.page.locator(MOB_SEARCH_SECOND_DROPDOWN.format(element)).click(force=True)
                except Exception as e:
                    print(e)

