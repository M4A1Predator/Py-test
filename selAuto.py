__author__ = 'Predator'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Sometime I wanted to know how many players were playing "Call of Duty"

# Use phantomJS as a browser
#driver = webdriver.PhantomJS("D:\\plusplus\\Tools\\phantomjs-2.0.0-windows\\bin\\phantomjs.exe")
# Use Firefox as a browser
driver = webdriver.Firefox()
driver.get("http://store.steampowered.com/stats/")
wait = WebDriverWait(driver, 20)
gameNames = "Call of Duty"

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='detailLink']")))
driver.find_element_by_xpath("//a[@id='detailLink']").click()

gameLinks = driver.find_elements_by_xpath("//div[@id='detailStats']/table/tbody/tr[@class='player_count_row']")
for i in gameLinks:
    game = str(i.text)
    if game.find(gameNames) != -1:
        print(game[:(str(i.text).find(" "))], end=" ")
        print(game[game.find(gameNames):])

driver.quit()
print("END")

