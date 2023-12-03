
from LoginPage import SearchHelper

def test_log_in(browser):
    lp = SearchHelper(browser)
    lp.go_to_site()
    lp.enter_login_field('standard_user')
    lp.enter_password('secret_sauce')
    lp.click_button()
    assert lp.get_word() == 'Products'