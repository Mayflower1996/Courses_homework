"""
Automation Script for Website Interactions.

This script automates interactions with a website using Selenium.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL, contact_payload, edited_payload


class BasePage:
    """Base class for Selenium page interactions."""

    def __init__(self, driver):
        """Initialize the BasePage with a WebDriver instance."""
        self.driver = driver

    def find_element(self, by, value):
        """Find and return an element identified by 'by' and 'value'."""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        """Find an element identified by 'by' and 'value', then click on it."""
        element = self.find_element(by, value)
        element.click()

    def send_keys_to_element(self, by, value, text):
        """Find an element identified by 'by' and 'value', then send 'text' to it."""
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)


class LoginPage(BasePage):
    """Class representing the login page."""

    def login(self, email, password):
        """Login to the system using provided 'email' and 'password'."""
        self.send_keys_to_element(By.ID, 'email', email)
        self.send_keys_to_element(By.ID, 'password', password)
        self.click_element(By.ID, 'submit')


class ContactPage(BasePage):
    """Class representing the contact page."""

    def add_contact(self, contact_details):
        """Add a contact using 'contact_details' dictionary."""
        self.click_element(By.ID, 'add-contact')
        for key, value in contact_details.items():
            self.send_keys_to_element(By.ID, key, value)
        self.click_element(By.ID, 'submit')

    def edit_contact(self, contact_details):
        """Edit a contact using 'contact_details' dictionary."""
        contact_row = self.find_element(By.CLASS_NAME, 'contactTableBodyRow')
        contact_row.click()
        edit_button = self.find_element(By.ID, 'edit-contact')
        edit_button.click()
        for key, value in contact_details.items():
            self.send_keys_to_element(By.ID, key, value)
        self.click_element(By.ID, 'submit')

    def delete_contact(self):
        """Delete a contact."""
        self.click_element(By.ID, 'delete')
        self.driver.switch_to.alert.accept()


browser = webdriver.Chrome()

browser.get(URL)
login_page = LoginPage(browser)
contact_page = ContactPage(browser)

login_page.login('jjgraffity@gmail.com', 'Vania1996123qwe')
contact_page.add_contact(contact_payload)
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'contactTableBodyRow')))

contact_page.edit_contact(edited_payload)
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'delete')))

contact_page.delete_contact()
browser.quit()
