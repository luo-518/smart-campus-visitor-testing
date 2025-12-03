import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def wait_for_hub(url, timeout=30):
    import requests
    for i in range(timeout):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return True
        except:
            pass
        time.sleep(1)
    raise Exception("Selenium Hub not ready")

def test_booking_flow():

    selenium_url = os.getenv("SELENIUM_REMOTE_URL")
    flask_url = os.getenv("FLASK_URL")

    # 等待 Hub 完全 ready
    wait_for_hub("http://selenium-hub:4444/status")

    # Selenium 4 Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=options
    )
