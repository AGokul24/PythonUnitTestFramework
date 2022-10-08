from selenium.webdriver.common.by import By

class AppointmentconfirmationPage():
    toggleMenuIcon_xpath = "//a[@id='menu-toggle']"
    LogoutBtn_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def clickToggleMenu(self):
        self.driver.find_element(By.XPATH, self.toggleMenuIcon_xpath).click()

    def clickLogoutBtn(self):
        self.driver.find_element(By.XPATH, self.LogoutBtn_xpath).click()
