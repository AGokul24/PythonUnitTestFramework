from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class HomePage:
    dropdown_id = "combo_facility"
    dropdown_xpath = "//select[@id='combo_facility']"
    medicaid_id = "radio_program_medicaid"
    medicaid_xpath = "//*[@id='radio_program_medicaid']"
    visitDate_id = "txt_visit_date"
    visitDate_xpath = "//input[@id='txt_visit_date']"
    comments_id = "txt_comment"
    comments_xpath = "//textarea[@id='txt_comment']"
    bookAppointment_xpath = "//button[@id='btn-book-appointment']"
    MakeAppointment_xpath = "//h2[contains(text(),'Make Apointment')]"

    def __init__(self, driver):
        self.driver = driver

    def dropdownOptionSelect(self, indexOfDropdown):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.MakeAppointment_xpath)))
        except TimeoutException:
            print("Timeout error has occurred, Element is not found in the UI. <br>")

        dropDown = Select(self.driver.find_element(By.XPATH, self.dropdown_xpath))
        dropDown.select_by_value(indexOfDropdown)


    def medicaidRadioSelection(self):
        self.driver.find_element(By.XPATH, self.medicaid_xpath).click()

    def visitDateOfPatient(self, visitDate):
        self.driver.find_element(By.XPATH, self.visitDate_xpath).send_keys(visitDate)

    def appointmentComments(self, comment):
        self.driver.find_element(By.XPATH, self.comments_xpath).send_keys(comment)

    def bookAppointmentBtn(self):
        self.driver.find_element(By.XPATH, self.bookAppointment_xpath).click()