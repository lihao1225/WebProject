from test_demo.page.addhomework_page import AddHomeWorkPage
from test_demo.page.main_page import MainPage


class TestAddHomeWork:

    def test_add_homework(self):
        main = MainPage().goto_login().login().goto_detail().goto_homework_tab().add_homework()
        assert "作业提交成功" == main
