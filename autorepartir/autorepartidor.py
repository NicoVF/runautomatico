from logging import error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import json
import smtplib
from colorama import init, Back, Style, Fore
init()

#Falta ponerle el horario al mail, hacer un bucle while y que repita todo cada 40 minutos.



chromeOptions = Options()
chromeOptions.headless = False
driver = webdriver.Chrome(executable_path=r"./chromedriver", options=chromeOptions)



    #URL="https://ferlamas.com/testbot/chatbot"  #página que no funciona
URL="https://delivery.run0km.com/login" #página que funciona

driver.get(URL)
    #driver.set_window_position(-2000, 0) #establece donde se abre la ventana
driver.maximize_window()

time.sleep(3)
   #link = driver.find_element_by_class_name("olark-button-text")
   #link.click()

try:

    login = driver.find_element_by_id("id_username")
    pw = driver.find_element_by_id("id_password")

    #repartiendo datos STD
    login.send_keys("user")
    pw.send_keys("pass")


    getin = driver.find_element_by_css_selector("input[type='submit']")
    getin.click()
    time.sleep(1)
    driver.get('https://delivery.run0km.com/admin/prospectos/prospecto/asignacion_inicial/')
    time.sleep(1)
    driver.find_element_by_id("id_asignar_segun_0").click()
    time.sleep(1)
    driver.find_element_by_id("id_metodo_por_productividad").click()
    time.sleep(1)
    driver.find_element_by_id("id_aplicar_restricciones_del_pedido").click()
    time.sleep(1)
    driver.find_element_by_id("id_restricciones_0").click()
    time.sleep(1)
    from datetime import datetime
    
    driver.find_element_by_id("id_fecha_desde").send_keys(datetime.today().strftime('%Y-%m-%d'))
    time.sleep(1)
    driver.find_element_by_id("id_accion").click()
    time.sleep(4)
    driver.find_element_by_css_selector("input[type='submit' i]").click()
    time.sleep(10)

    #repartiendo datos STD y PREM por supervisor
    driver.get('https://delivery.run0km.com/admin/prospectos/prospecto/asignacion_inicial/')
    time.sleep(1)
    driver.find_element_by_id("id_asignar_segun_0").click()
    time.sleep(1)
    driver.find_element_by_id("id_metodo_por_productividad").click()
    time.sleep(1)
    driver.find_element_by_id("id_aplicar_restricciones_del_pedido").click()
    time.sleep(1)
    from datetime import datetime
    
    driver.find_element_by_id("id_fecha_desde").send_keys(datetime.today().strftime('%Y-%m-%d'))
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='id_accion']/option[2]").click()
    time.sleep(1)
    driver.find_element_by_id("id_accion").click()
    time.sleep(4)
    #driver.find_element_by_css_selector("input[type='submit' i]").click()
    time.sleep(10)


    #repartiendo datos PREM
    driver.get('https://delivery.run0km.com/admin/prospectos/prospecto/asignacion_inicial/')
    time.sleep(1)
    driver.find_element_by_id("id_asignar_segun_0").click()
    time.sleep(1)
    driver.find_element_by_id("id_metodo_por_productividad").click()
    time.sleep(1)
    driver.find_element_by_id("id_aplicar_restricciones_del_pedido").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='id_origen']/option[3]").click()
    time.sleep(1)
    from datetime import datetime
    
    driver.find_element_by_id("id_fecha_desde").send_keys(datetime.today().strftime('%Y-%m-%d'))
    time.sleep(1)
    driver.find_element_by_id("id_accion").click()
    time.sleep(4)
    
    driver.find_element_by_css_selector("input[type='submit' i]").click()
    time.sleep(8)
    

    #Tirando sobrante
    driver.get('https://delivery.run0km.com/admin/prospectos/prospecto/asignacion_inicial/')
    time.sleep(1)
    driver.find_element_by_id("id_asignar_segun_1").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='id_accion']/option[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='id_responsables']/option[121]").click()
    time.sleep(1)
    from datetime import datetime
    
    driver.find_element_by_id("id_fecha_desde").send_keys(datetime.today().strftime('%Y-%m-%d'))
    time.sleep(1)
    driver.find_element_by_id("id_accion").click()
    time.sleep(4)
    
    #antes de repartir, revisar cuantos sobraron
    #driver.find_element_by_css_selector("input[type='submit' i]").click()
    time.sleep(13)
    
    

    


except:
    print("algo fallo", sys.exc_info()[0], " error")
    time.sleep(1)


    
print("finish")