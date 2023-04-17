def main():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.by import By
    from datetime import datetime
    import sys
    import time
    import json
    
    print("--- AUTOREPARTIDOR ---")
    print(f"Delivering at {datetime.today().strftime('%Y-%m-%d')}")
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
    #find_element(By.Class, "nameclass")
    #link.click()

    try:
        with open("credenciales.json") as file:
            credentials = json.load(file)
        driver.find_element(By.ID, "id_username").send_keys(credentials["username"])
        driver.find_element(By.ID,"id_password").send_keys(credentials["password"])
        getin = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
        getin.click()
        time.sleep(1)
        driver.get('https://delivery.run0km.com/admin/prospectos/prospecto/asignacion_inicial/')
        time.sleep(1)
        #Repartiendo usado y jeep
        actions = ActionChains(driver)

        actions.key_down(Keys.CONTROL)
        driver.find_element(By.XPATH, f"//div[@id='categorias_container']/select/option[@value='231']").click()
        '''
        categoriasID = [231]
        for catId in categoriasID:
            driver.find_element(By.XPATH, f"//div[@id='categorias_container']/select/option[@value='{catId}']").click()
        '''
        actions.key_up(Keys.CONTROL)
        time.sleep(1)        
        driver.find_element(By.ID,"id_asignar_segun_0").click()
        time.sleep(1)        
        driver.find_element(By.ID,"id_metodo_por_productividad").click()
        time.sleep(1)
        driver.find_element(By.ID,"id_aplicar_restricciones_del_pedido").click()
        time.sleep(1)
        driver.find_element(By.ID,"id_restricciones_0").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input[type='submit' i]").click()
        time.sleep(120)
        #driver.close()

    except Exception as e:
        print("algo fallo", e, " error")
        time.sleep(1)


        
    print(f"finished at {datetime.today().strftime('%Y-%m-%d')}")

main()