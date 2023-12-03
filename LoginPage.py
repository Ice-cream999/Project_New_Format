from BaseApp import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators():

    LOCATOR_USER_NAME_FIELD = (By.XPATH, "//input[@id='user-name']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOCATOR_BUTTON_LOGIN = (By.XPATH, "//input[@id='login-button']")
    LOCATOR_WORD = (By.XPATH, "//span[@class='title']")

class SearchHelper(BasePage):

    def enter_login_field(self, login):
        login_field = self.find_element(LoginPageLocators.LOCATOR_USER_NAME_FIELD)
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(LoginPageLocators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)
        return password_field

    def click_button(self):
        button = self.find_element(LoginPageLocators.LOCATOR_BUTTON_LOGIN)
        return button.click()

    def get_word(self):
        word_text = self.find_element(LoginPageLocators.LOCATOR_WORD).text
        return word_text






