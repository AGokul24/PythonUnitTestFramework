from selenium.webdriver.common.by import By

class LoginPage():
    textbox_username_id = "txt-username"
    textbox_password_id = "txt-password"
    login_btn_xpath = "//button[@id='btn-login']"
    toggleMenuIcon_xpath = "//a[@id='menu-toggle']"
    #loginHyperlink_xpath = "//a[contains(text(),'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
