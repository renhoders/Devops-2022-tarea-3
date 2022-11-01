from traceback import print_list
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import googletrans
from selenium.webdriver.support import expected_conditions as EC
import time

#configuracion driver y chrome desde linux mint
# nos aseguramos que la version de chromedriver aguante la version de chrome
driver_location = '/usr/bin/chromedriver'
binary_location = '/usr/bin/google-chrome'

#traducimos el texto todos las clases .review
#iniciamos googletrans , sudo pipe3 install googletrans 4.0.0rc1
translator = googletrans.Translator()

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location,options=options)

#mi contexto local
driver.get("http://127.0.0.1:8080/")


#agregamos las 2 peliculas.
driver.find_element(By.ID, "add-movie").click()
driver.find_element(By.NAME, "title").send_keys("Forrest Gump")
driver.find_element(By.NAME, "year").send_keys("1994")
driver.find_element(By.NAME, "director").send_keys("Robert Zemeckis")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME,"review").send_keys("Mientras espera sentado en una parada de autobús, Forrest Gump comienza a relatar la historia de su vida a diversos extraños que se sientan junto a él.")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

driver.find_element(By.ID, "add-movie").click()
driver.find_element(By.NAME, "title").send_keys("Rescatando al soldado Ryan")
driver.find_element(By.NAME, "year").send_keys("1998")
driver.find_element(By.NAME, "director").send_keys("Steven Spielberg")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME,"review").send_keys("En la mañana del 6 de junio de 1944, comienzo de la invasión de Normandía, los soldados estadounidenses se preparan para desembarcar en la playa de Omaha.")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

nums = [1, 2] #identidicadores de las peliculas para traducir
#contatenamos la id de las peliculas y traducimos su review
#finalmente guardamos.
for n in nums:
    url = "/edit/"+str(n)
    driver.find_element(By.XPATH,'//a[@href="'+url+'"]').click()
    txtAreaReview = driver.find_element(By.NAME, "review")
    txtAreaReview.clear()
    txtAreaReview.send_keys(translator.translate(txtAreaReview.text,dest='es').text)
    driver.find_element(By.CSS_SELECTOR, ".btn").click()

driver.quit()





