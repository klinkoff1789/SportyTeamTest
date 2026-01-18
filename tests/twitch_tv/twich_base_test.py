from playwright.sync_api import Page

from locators.media_locators import MOB_SEARCH_SECOND_DROPDOWN, mob_banners_button_names, MOB_SEARCH_ICON, \
    mob_banners_get_by_txt


class TwitchPopupManager:
    """
    A modular handler to clear all obstructions on m.twitch.tv
    before the stream begins.
    """

    def __init__(self, page: Page):
        self.page = page

    def register_all_handlers(self):
        """
        Registers background listeners for all known Twitch mobile popups.
        Playwright will pause execution, run these handlers, and resume
        automatically whenever these elements appear.
        """
        print("[Framework] Registering popup handlers...")

        # 1. Cookie Consent Banner
        # Priority: High (Blocks everything)
        self.page.add_locator_handler(
            self.page.locator('[data-a-target="consent-banner-accept"]'),
            self._handle_cookie_consent
            )

        # 2. "Open in the Twitch App" Banner (For a few languages)
        for txt in mob_banners_get_by_txt:
            self.page.add_locator_handler(
                self.page.get_by_text(txt),
                self._handle_twitch_app_banner
                )

    # --- Handler Implementations ---

    def _handle_cookie_consent(self):
        print("-> Detected Cookie Banner. Dismissing...")
        self.page.locator('[data-a-target="consent-banner-accept"]').click()

    def _handle_twitch_app_banner(self):
        print("-> Detected 'Open in the Twitch App'. Dismissing...")
        for name in mob_banners_button_names:
            _btn = self.page.get_by_role("button", name=name)
            _btn.click() if _btn.is_visible() else None


class TwitchPageActions:
    def __init__(self, page: Page):
        self.page = page

    def mob_scroll_down2(self, element=2):
        """
        :param element: element is an integer start with 2,
        scroll down to the element in dropdown search results
        (defaults to 2)
        """
        for i in range(1, element + 1):
            self.page.mouse.down()
            print(f"Scrolling down the {i} time")
            if i == element:
                select_locator = self.page.locator(MOB_SEARCH_SECOND_DROPDOWN.format(element))
                try:
                    select_locator.click()
                except Exception as e:
                    print(e)

    def get_clear_search(self):
        """If popups appear, the handlers will kill them
        before this timeout expires.
        """
        try:
            print("Waiting for Search icon visible and to clear obstructions...")
            # We wait for the Search icon element to be stable
            self.page.wait_for_selector(MOB_SEARCH_ICON, state="visible", timeout=15000)

        except Exception as e:
            print(f"Failed to reach Search icon for click. Error: {e}")
            self.page.screenshot(path="debug_error.png")
