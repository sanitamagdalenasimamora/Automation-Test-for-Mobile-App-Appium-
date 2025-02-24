from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest

class TestCekTarif:
    def setup_method(lionuser):
        """Setup desired capabilities and Appium server connection."""
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Google Nexus 4",
            "app": "D:/Lion Parcel Test/file apk/lionparcel.apk",
            "appPackage": "com.lionparcel.mobile",
            "appActivity": "com.lionparcel.mobile.MainActivity",
            "automationName": "UiAutomator2"
        }
        lionuser.driver = webdriver.Remote("http://localhost:4724/wd/hub", desired_caps)
        lionuser.driver.implicitly_wait(10)

    def teardown_method(lionuser):
        """Close App after test."""
        lionuser.driver.quit()

    def test_cek_tarif_positive(lionuser):
        """Test positif: Cek tarif dengan input valid."""
        lionuser.driver.find_element(AppiumBy.ID, "com.lionparcel.mobile:id/menu_cek_tarif").click()
        lionuser.driver.find_element(AppiumBy.ID, "com.lionparcel.mobile:id/input_asal").send_keys("Jakarta")


