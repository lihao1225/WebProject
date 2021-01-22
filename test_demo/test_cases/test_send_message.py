from test_demo.page.main_page import MainPage


class TestSendMessage:

    def test_send_message(self):
        main = MainPage().goto_login().login().goto_detail().goto_private_letter().send_message()
