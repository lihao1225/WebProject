from test_demo.page.main_page import MainPage


class TestLogin:

    def test_login(self):
        main = MainPage().goto_login().login().goto_detail()
