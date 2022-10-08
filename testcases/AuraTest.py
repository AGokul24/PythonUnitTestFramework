import json
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
from datetime import datetime
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

sys.path.append("C:/Users/Gokul A/PycharmProjects/pythonUnittestPOMProject")
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.AppointmentConfirmationPage import AppointmentconfirmationPage


class AuraTest(unittest.TestCase):
    #Import Json elements
    with open('C:/Users/Gokul A/PycharmProjects/pythonUnittestPOMProject/Testdata/AuraData.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)

    baseUrl = str(obj['baseUrl'])
    username = str(obj['username'])
    password = str(obj['password'])
    indexOfDropdown = str(obj['indexOfDropdown'])
    # Get current date
    now = datetime.now()
    visitDate = now.strftime("%d-%m-%Y")
    comment = str(obj['comment'])
    # chrome
    #driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    # FireFox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()

    def test_01_login(self):
        objectLoginPage = LoginPage(self.driver)
        objectLoginPage.setUserName(self.username)
        objectLoginPage.setPassword(self.password)
        objectLoginPage.clickLogin()
        time.sleep(5)
        # validation
        self.assertEqual("CURA Healthcare Service", self.driver.title, "Webpage title is not matching")
        #verification
        BookAppointmentBtn = self.driver.find_element(By.XPATH, "//button[@id='btn-book-appointment']")
        if BookAppointmentBtn.is_displayed():
            print("User session logged in with : "+self.username)
        else:
            print("User session failed to logged in")

    def test_02_bookAppointment(self):
        ObjectHomePage = HomePage(self.driver)
        ObjectHomePage.dropdownOptionSelect(self.indexOfDropdown)
        ObjectHomePage.medicaidRadioSelection()
        ObjectHomePage.visitDateOfPatient(self.visitDate)
        ObjectHomePage.appointmentComments(self.comment)
        ObjectHomePage.bookAppointmentBtn()
        #Verification
        time.sleep(5)
        VerificationComment = self.driver.find_element(By.XPATH, "//p[@id='comment']").text
        if self.comment == VerificationComment:
            print("Appointment successfully Booked")
        else:
            print("Appointment booking failed")

    def test_03_logout(self):
        ObjectConfirm = AppointmentconfirmationPage(self.driver)
        ObjectConfirm.clickToggleMenu()
        ObjectConfirm.clickLogoutBtn()
        # Verification
        time.sleep(5)
        MakeAppointmentBtn = self.driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
        if MakeAppointmentBtn.is_displayed():
            print("User session logged out and reached the home page")
        else:
            print("User session failed to logout")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Login Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:\\Users\\Gokul A\\PycharmProjects\\pythonUnittestPOMProject\\Reports'))
