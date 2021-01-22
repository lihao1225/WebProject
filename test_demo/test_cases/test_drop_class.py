from test_demo.page.main_page import MainPage


class Test_Drop_Class:

    def test_drop_class(self):
        main = MainPage().goto_login().login().drop_class()
