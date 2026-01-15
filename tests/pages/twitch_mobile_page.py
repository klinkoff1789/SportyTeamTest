import re

from playwright.sync_api import Page, expect
from locators.media_locators import COOKIES_ACCEPT_BUTTON, MOB_SEARCH_ICON, MOB_SEARCH_FIELD

class TwitchMobilePage:
    def __init__(self, page: Page):
        self.page = page
        self.mouse = page.mouse
        self.locator = page.locator

    #TODO has to be covered by unittests
    def open(self):
        self.page.goto("https://www.twitch.tv/")
        expect(self.page).to_have_title(re.compile("Twitch"))
        return self

    #TODO has to be covered by unittests
    @property
    def cookies_popup(self):
        popup_accept = self.page.locator(
            COOKIES_ACCEPT_BUTTON).first
        return popup_accept

    #TODO has to be covered by unittests
    @property
    def mob_search_icon(self):
        mob_search_icon = self.page.locator(MOB_SEARCH_ICON)
        return mob_search_icon

    #TODO has to be covered by unittests
    @property
    def mob_search_field(self):
        mob_search_field = self.page.locator(MOB_SEARCH_FIELD)
        return mob_search_field

    # @property
    # def mob_search_dropdown(self):
    #     """Hardcoded mob search field 2"""
    #     mob_search_dropdown = self.page.locator(MOB_SEARCH_SECOND_DROPDOWN)
    #     return mob_search_dropdown
    # def wait_for_load_state(self, param):
    #     pass
    #
    # def screenshot(self, path):
    #     pass
