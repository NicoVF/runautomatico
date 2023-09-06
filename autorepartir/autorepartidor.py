from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from mailsender.mailsender import MailSender
import sys
sys.path.append('..//mailsender')
from mailsender import MailSender
import datetime
import time
import json


def repartir_datos_STD(driver, imagenes, con_fecha_de_hoy=True):
    open_url(credentials["repartir_url"], driver)
    time.sleep(1)
    driver.find_element(By.ID, "id_asignar_segun_0").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_metodo_por_productividad").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_aplicar_restricciones_del_pedido").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_restricciones_0").click()
    time.sleep(1)
    nombre_de_screenshot = "STD sin fecha"
    if con_fecha_de_hoy:
        driver.find_element(By.ID, "id_fecha_desde").send_keys(fecha_actual)
        time.sleep(4)
        nombre_de_screenshot = "STD con fecha de HOY"
    driver.find_element(By.CSS_SELECTOR, "input[type='submit' i]").click()
    time.sleep(10)
    take_screenshot(driver, imagenes, nombre_de_screenshot)
    print(f"Se repartio {nombre_de_screenshot} a las {current_time_with_seconds()}")


def repartir_datos_STD_y_PREM_por_SUPERVISOR(driver, imagenes, con_fecha_de_hoy=True):
    open_url(credentials["repartir_url"], driver)
    time.sleep(1)
    driver.find_element(By.ID, "id_asignar_segun_0").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_metodo_por_productividad").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_aplicar_restricciones_del_pedido").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_restricciones_0").click()
    time.sleep(1)
    nombre_de_screenshot = "STD y PREM por SUPERVISOR sin fecha"
    if con_fecha_de_hoy:
        driver.find_element(By.ID, "id_fecha_desde").send_keys(fecha_actual)
        time.sleep(4)
        nombre_de_screenshot = "STD y PREM por SUPERVISOR con fecha de HOY"
    driver.find_element(By.XPATH, "//*[@id='id_accion']/option[2]").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_accion").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit' i]").click()
    time.sleep(10)
    take_screenshot(driver, imagenes, nombre_de_screenshot)
    print(f"Se repartio {nombre_de_screenshot} a las {current_time_with_seconds()}")


def repartir_datos_PREM(driver, imagenes, con_fecha_de_hoy=True):
    open_url(credentials["repartir_url"], driver)
    driver.find_element(By.ID, "id_asignar_segun_0").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_metodo_por_productividad").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_aplicar_restricciones_del_pedido").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='id_origen']/option[3]").click()
    time.sleep(1)
    nombre_de_screenshot = "PREM sin fecha"
    if con_fecha_de_hoy:
        driver.find_element(By.ID, "id_fecha_desde").send_keys(fecha_actual)
        time.sleep(1)
        nombre_de_screenshot = "PREM con fecha de HOY"
    driver.find_element(By.ID, "id_accion").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit' i]").click()
    time.sleep(10)
    take_screenshot(driver, imagenes, nombre_de_screenshot)
    print(f"Se repartio {nombre_de_screenshot} a las {current_time_with_seconds()}")


def tirar_sobrante_con_fecha_de_hoy(driver, imagenes):
    open_url(credentials["repartir_url"], driver)
    driver.find_element(By.ID, "id_asignar_segun_1").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='id_accion']/option[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//select[@id='id_responsables']/option[@value='4704']").click()
    time.sleep(1)
    driver.find_element(By.ID, "id_fecha_desde").send_keys(fecha_actual)
    time.sleep(1)
    driver.find_element(By.ID, "id_accion").click()
    time.sleep(4)
    driver.find_element_by_css_selector("input[type='submit' i]").click()
    time.sleep(13)


def send_email(imagenes):
    mensaje = "Se forzaron los siguientes datos:"
    fecha_y_hora_actual = current_date() + " " + current_time()
    mail_sender = MailSender(credentials["email_sender_username"], credentials["email_pass"])
    mail_sender.send(credentials["email_sender_username"], credentials["email_receivers"],
                     f"Forzado automatico - {fecha_y_hora_actual}", message=mensaje, images=imagenes)
    print(f"\nSe envio un email a {credentials['email_receivers'][0]} a las {current_time()} con las imagenes:\n")
    for imagen in imagenes:
        print(f"{imagen}")


def take_screenshot(driver, imagenes, nombre):
    fecha_y_hora_actual = current_date() + " " + current_time_with_seconds()
    driver.get_screenshot_as_file(f"screenshots/{fecha_y_hora_actual.replace(':','.') + ' - ' + nombre}.png")
    imagenes.append(f"screenshots/{fecha_y_hora_actual.replace(':','.') + ' - ' + nombre}.png")


def login(driver):
    driver.find_element(By.ID, "id_username").send_keys(credentials["action"])
    driver.find_element(By.ID, "id_password").send_keys(credentials["directory"])
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


def get_webdriver():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("detach", True)
    seleniumService = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=seleniumService, options=chromeOptions)
    return driver


def open_url(URL, driver):
    time.sleep(1)
    driver.get(URL)
    driver.maximize_window()
    time.sleep(3)


def current_date():
    return str(datetime.datetime.now().strftime('%Y-%m-%d'))


def current_time():
    return str(datetime.datetime.now().strftime('%H:%M'))


def current_time_with_seconds():
    return str(datetime.datetime.now().strftime('%H:%M:%S'))


fecha_actual = current_date()

print("--- AUTOREPARTIDOR ---")
print(f"\nFecha: {fecha_actual + ' ' +current_time()}\n")

driver = get_webdriver()
imagenes = list()

try:
    with open("../credenciales.json") as file:
        credentials = json.load(file)

    open_url(credentials["login_url"], driver)
    login(driver)
    repartir_datos_STD(driver, imagenes)
    repartir_datos_STD(driver, imagenes, con_fecha_de_hoy=False)
    repartir_datos_STD_y_PREM_por_SUPERVISOR(driver, imagenes)
    repartir_datos_STD_y_PREM_por_SUPERVISOR(driver, imagenes, con_fecha_de_hoy=False)
    repartir_datos_PREM(driver, imagenes)
    repartir_datos_PREM(driver, imagenes, con_fecha_de_hoy=False)
    send_email(imagenes)

except Exception as e:
    print("Error al repartir los datos: ", e)
    time.sleep(1)

driver.close()
driver.quit()

