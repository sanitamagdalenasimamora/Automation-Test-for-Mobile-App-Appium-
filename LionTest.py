from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# Konfigurasi Desired Capabilities
desired_caps = {
    "appium:platformName": "Android",
    "appium:deviceName": "Google Nexus 4",
    "appium:appPackage": "com.lionparcel.services.consumer",
    "appium:appActivity": "/com.lionparcel.services.consumer.view.main.MainActivity",
    "appium:automationName": "iuautomatior2"
}

# Inisialisasi driver
driver = webdriver.Remote("http://localhost:4725/wd/hub", desired_caps)
time.sleep(5)
