from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver=  webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.python.org")
assert "Python" in driver.title
print("asserted")
