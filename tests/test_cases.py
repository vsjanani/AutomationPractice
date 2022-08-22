import pytest
from selenium import webdriver


@pytest.mark.usefixtures("begin_end")
class TestShopping:
    def test_f2208_ap_url_title(self):
        assert(self.webdriver_obj.title == "My Store")



