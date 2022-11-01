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

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location,options=options)

driver.get("http://127.0.0.1:8080/")

#traducimos el texto todos las clases .review
#iniciamos googletrans , sudo pipe3 install googletrans 4.0.0rc1
translator = googletrans.Translator()

#obtenemos todos los componentes que cumplan con .review
reviews = driver.find_elements(By.XPATH, "//p[@class='review']")

#recorremos el arreglo reviews para poder traducir de Ingles a Espaniol
for review in reviews:
    driver.execute_script("arguments[0].textContent = arguments[1];", review, translator.translate(review.text,dest='es').text)

time.sleep(5)

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

time.sleep(5)

driver.quit()





