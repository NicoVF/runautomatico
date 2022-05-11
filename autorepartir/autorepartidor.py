def main():
        
    print("--- AUTOREPARTIDOR ---")
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.by import By
    import sys
    import time
    import json


    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.headless = False
    chromeOptions.add_experimental_option("detach", True)
    seleniumService = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=seleniumService, options=chromeOptions)

    URL="https://delivery.run0km.com/login" #página que funciona

    driver.get(URL)
        #driver.set_window_position(-2000, 0) #establece donde se abre la ventana
    driver.maximize_window()

    time.sleep(3)
    #link = driver.find_element_by_class_name("olark-button-text")
    #link.click()

    try:

        with open("credenciales.json") as file:
            credentials=json.load(file)
        driver.find_element_by_id("id_username").send_keys(credentials["username"])
        driver.find_element_by_id("id_password").send_keys(credentials["password"])
            
        #repartiendo datos STD
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
        driver.find_element_by_xpath("//select[@id='id_responsables']/option[@value='4704']").click()
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