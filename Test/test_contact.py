from Menus.contact import Contact_Us


def test_contact(driver):
    # object of Contact_Us class
    cu = Contact_Us(driver)
    # test contact us page
    cu.click_contact_us()
    #test hover over text
    cu.hover_over_event()


