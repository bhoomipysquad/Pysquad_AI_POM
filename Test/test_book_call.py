from Menus.Book_call import Book_Call


def test_book_call(driver):
    # object of Book_call
    book = Book_Call(driver)

    # test book_call button
    book.click_book_call()