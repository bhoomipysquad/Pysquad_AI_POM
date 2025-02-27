from Menus.Social_media_page import Social_Media


def test_social_media(driver):
    sm = Social_Media(driver)
    #test social media pages
    sm.open_social_media_pages()
