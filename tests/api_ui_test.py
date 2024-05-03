from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_ui():
    driver = webdriver.Chrome()  # Change to the appropriate driver
    driver.get("http://127.0.0.1:5000/login")  # Update with your app's URL

    username_field = driver.find_element(By.ID, "username")  # Update with the ID of the username field
    username_field.send_keys("test_user")

    password_field = driver.find_element(By.ID, "password")  # Update with the ID of the password field
    password_field.send_keys("password")
    password_field.send_keys(Keys.RETURN)

    time.sleep(5)  # Replace with more reliable waits (e.g., WebDriverWait)
    assert driver.current_url == "http://127.0.0.1:5000/"  # Update with the expected URL

    driver.quit()

if __name__ == "__main__":
    test_login_ui()
