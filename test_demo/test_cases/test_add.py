from test_demo.page.main_page import MainPage


class TestAdd:

    def test_add(self):
        main = MainPage().goto_login().login().add_class()
