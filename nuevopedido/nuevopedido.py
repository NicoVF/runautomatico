def main():

        print("--- ARMADOR DE PEDIDOS ---")
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
        from selenium.webdriver.common.by import By
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options
        from datetime import datetime
        import time
        import sys
        import json

        time.sleep(6)

        nombre_del_pedido = input('Nombre del concesionario? ').capitalize()
        nombre_del_supervisor = input('Nombre del supervisor? No olvides los acentos ')
        nta = nombre_del_supervisor.split(' ')
        credito = input('Cantidad de credito: ')
        aCargo = input('El pedido es a cargo del supervisor? Si/No: ').lower()
        marca = input('Marca? ').lower()
        tiene_prefijos = input("Incluye prefijos? Si/No: ").lower()
        terminarAlgoritmo = False

        if(tiene_prefijos == 'si'):
                prefijos = ["351","353","2336","3382","3385","3387","3463","3467","3468","3472","351","3521","3522","3524","3525","353","3532","3533","3537","3541","3542","3543","3544","3546","3547","3548","3549","3562","3563","3564","3571","3572","3573","3574","3575","3576","358","3582","3583","3584","3585","3564","266","265","358","2657","351","3564","0351","0353","02336","03382","03385","03387","03463","03467","03468","03472","0351","03521","03522","03524","03525","0353","03532","03533","03537","03541","03542","03543","03544","03546","03547","03548","03549","03562","03563","03564","03571","03572","03573","03574","03575","03576","0358","03582","03583","03584","03585","03564","0266","0265","0358","02657","0351","03564","00351","00353","002336","003382","003385","003387","003463","003467","003468","003472","00351","003521","003522","003524","003525","00353","003532","003533","003537","003541","003542","003543","003544","003546","003547","003548","003549","003562","003563","003564","003571","003572","003573","003574","003575","003576","00358","003582","003583","003584","003585","003564","00266","00265","00358","002657","00351","003564"]

        counter = 0

        
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.headless = False
        chromeOptions.add_experimental_option("detach", True)
        seleniumService = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=seleniumService, options=chromeOptions)
        
        driver.get("https://delivery.run0km.com/login")
        driver.maximize_window()

        try:
                
                with open("credenciales.json") as file:
                        credentials=json.load(file)
                driver.find_element_by_id("id_username").send_keys(credentials["username"])
                driver.find_element_by_id("id_password").send_keys(credentials["password"])
                getin = driver.find_element_by_css_selector("input[type='submit']")
                getin.click()
                while terminarAlgoritmo == False:
                        time.sleep(2)
                        driver.get(
                                "https://delivery.run0km.com/admin/prospectos/pedidodeprospecto/add/")
                        time.sleep(10)

                        # campo
                        if(tiene_prefijos == 'si'):
                                driver.find_element_by_id('id_factor_de_distribucion').clear()
                                driver.find_element_by_id('id_factor_de_distribucion').send_keys('150')

                                for i in prefijos:
                                        driver.find_element_by_xpath(
                                                "//a[.='Agregar otro/a Filtro de pedido']").click()
                                        counter = counter + 1

                                time.sleep(1)
                                # counter
                                print("counter: ", counter)
                                for i in range(counter):
                                        path = "//td[@class='field-campo']/input[contains(@name,'filtros-"+str(
                                                i)+"')]"
                                        driver.find_element_by_xpath(path).send_keys("telefono")

                        # accion
                                for i in range(counter):
                                        path = "//td[@class='field-accion']/select[contains(@name,'filtros-"+str(
                                                i)+"')]/option[@value='I']"
                                        driver.find_element_by_xpath(path).click()

                        # selector
                                for i in range(counter):
                                        path = "//td[@class='field-selector']/select[contains(@name,'filtros-"+str(
                                                i)+"')]/option[@value='pre']"
                                        driver.find_element_by_xpath(path).click()

                        # valor
                                for i in range(0, len(prefijos)):
                                        path = "//td[@class='field-valor']/input[contains(@name,'filtros-"+str(
                                                i)+"')]"
                                        driver.find_element_by_xpath(path).send_keys(prefijos[i])

                        time.sleep(1)

                        if(aCargo == 'si'):
                                driver.find_element_by_xpath('//*[@id="id_asignar_a"]/option[3]').click()
                        else:
                                driver.find_element_by_xpath('//*[@id="id_asignar_a"]/option[2]').click()

                        if(tiene_prefijos == 'no'):
                                if(aCargo == 'si'):
                                        driver.find_element_by_id('id_restringir_por_datos_diarios').click()
                                        driver.find_element_by_id('id_restringir_por_acceso').click()
                                else:
                                        driver.find_element_by_id('id_restringir_por_datos_nuevos').click()
                                        driver.find_element_by_id('id_restringir_por_datos_diarios').click()
                                        driver.find_element_by_id('id_restringir_por_acceso').click()
                        else:
                                driver.find_element_by_id('id_restringir_por_acceso').click()

                        
                        driver.find_element_by_id('id_nombre').send_keys(
                                marca+'-std-'+nombre_del_pedido.lower().replace(' ', '-')+'-'+nta.pop().lower()
                                )
                        driver.find_element_by_id('id_credito').send_keys(credito)

                        try:
                                driver.find_element_by_id("id_fecha").send_keys(
                                datetime.today().strftime('%d/%m/%Y'))
                        except Exception as e:
                                print("No fue posible agregar la fecha, error: ",e)
                                        

                        time.sleep(1)
                        opt_std_mailing = driver.find_element_by_xpath(
                                '//*[@id="id_categorias"]/option[4]')
                        opt_std_run = driver.find_element_by_xpath(
                                '//*[@id="id_categorias"]/option[59]')

                        from selenium.webdriver.common.action_chains import ActionChains

                        time.sleep(1)

                        try:
                                driver.find_element_by_id('id_metodo_de_asignacion_3').click()
                        except Exception as e:
                                print("No fue posible agregar prefijos, error: ",e)

                        time.sleep(1)

                        try:
                                driver.find_element_by_xpath('//*[@id="id__calidades"]/option[3]').click()
                                ActionChains(driver) \
                                        .key_down(Keys.CONTROL) \
                                        .click(opt_std_mailing) \
                                        .click(opt_std_run) \
                                        .key_up(Keys.CONTROL) \
                                        .perform()
                        except Exception as e:
                                        print("No fue posible agregar calidades, error: ",e)

                        time.sleep(1)
                        try:
                                super_path = "//*[@id='id_supervisor']/option[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'" + \
                                        nombre_del_supervisor+"')]"
                                driver.find_element_by_xpath(super_path).click()
                        except Exception as e:
                                        print("No fue posible agregar al supervisor, error: ",e)
                        
                        if(tiene_prefijos == 'si'):
                                try:
                                        # no funciona <class 'selenium.common.exceptions.NoSuchElementException'> error
                                        driver.find_element_by_xpath(
                                                "//a[.='Agregar otro/a Filtro de pedido']").click()
                                        indexMarca = str(counter+1)
                                        print("index marca es: " + indexMarca)
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-accion']/select[contains(@name,'filtros-"+indexMarca+"')]/option[@value='I']").click()
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-campo']/input[contains(@name,'filtros-"+indexMarca+"')]").send_keys("marca")
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-selector']/select[contains(@name,'filtros-"+indexMarca+"')]/option[@value='in']")
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-valor']/input[contains(@name,'filtros-"+indexMarca+"')]").send_keys(marca)
                                except Exception as e:
                                        print("No fue posible agregar prefijos, error: ",e)
                                        
                        else:
                                try:
                                        driver.find_element_by_xpath(
                                                "//a[.='Agregar otro/a Filtro de pedido']").click()
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-accion']/select[contains(@name,'filtros-"+str(counter)+"')]/option[@value='I']").click()
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-campo']/input[contains(@name,'filtros-"+str(counter)+"')]").send_keys("marca")
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-selector']/select[contains(@name,'filtros-"+str(counter)+"')]/option[@value='in']").click()
                                        driver.find_element_by_xpath(
                                                "//td[@class='field-valor']/input[contains(@name,'filtros-"+str(counter)+"')]").send_keys(marca)
                                except Exception as e:
                                        print("No fue posible agregar filtros de pedido como marca solicitada, error : ",e)



                        terminar = input("Tiene mas pedidos para cargar?")
                        if(terminar.lower() == "No"):
                                terminarAlgoritmo = True
        except:
                print("algo fallo", sys.exc_info()[0], "error")
