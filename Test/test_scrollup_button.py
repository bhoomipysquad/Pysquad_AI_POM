from Menus.check_scrollup_button import Check_ScrollUp_Button


def test_contact(driver):
    su = Check_ScrollUp_Button(driver)
    #test scroll up button
    su.check_scrollup_button()