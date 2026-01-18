#Twitch page locators
COOKIES_ACCEPT_BUTTON = '//button[contains(@class,"ScCoreButton")]/div[contains(@class, "ScCoreButtonLabel")]'
MOB_SEARCH_ICON ='//*[name()="path" and contains(@d, "M2 10.5a8.5 8.5 0 1 1 15.176")]'
MOB_SEARCH_FIELD = '//*/input["Search"]'
MOB_SEARCH_SECOND_DROPDOWN = '//*//li[{}]/a//p[contains(@title, "StarCraft II")]'

# Due to testing in 2 languages added two variants ONLY
mob_banners_get_by_txt = ["Open in the Twitch App", "Відкрити в мобільній програмі Twitch"]
mob_banners_button_names = ["Dismiss", "Відхилити"]

# Text to type
SEARCH_TXT = "StarCraft II"
