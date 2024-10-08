import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        assert row2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row2_input_element.send_keys("Pie")

        # Push Save button using locator By.name(“Save”)
        save_button_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        save_button_locator.click()

        # Verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation massage is not expected"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(5)

        # Clear input field
        row1_edit_button = driver.find_element(By.ID, "edit_btn")
        row1_edit_button.click()

        row1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row1_input_element))
        row1_input_element.clear()

        # Type text into the input field
        row1_input_element.send_keys("Pie")

        row1_save_button = driver.find_element(By.ID, "save_btn")
        row1_save_button.click()

        # Verify text changed
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation massage is not expected"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), "Instructions text element should not be displayed")

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        row2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
                                        "Failed waiting for row 2 input to be visible")

        # Verify second input field is displayed
        assert row2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
