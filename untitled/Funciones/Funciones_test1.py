import click.testing
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import tracemalloc
import requests



dato = None

class Funciones_global():
    None
    '''
    def __init__(self, driver):
        self.driver=driver

    def Tiempo(self, tie):
        t=time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Pagina abierta: " + str(Url))
        t = time.sleep(Tiempo)
        return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element("xpath", elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("ID", elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element("ID", elemento)
        return val

    def texto_xpath_valida(self, xpath, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)
            #val = ActionChains(self.driver)
            #val.move_to_element(val).perform()
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo el texto {} ".format(texto))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)

    ## Tomamos texto como parametro que usaremos
    def Get_texto_xpath(self, xpath, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)
            dato = val.text
            print("Escribiendo en el campo el texto {} ".format(dato))
            t = time.sleep(Tiempo)
            return t, dato
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)


    #def Select_xpath_type(self, xpath, tipo, dato, Tiempo):
    def Select_xpath_type(self, xpath, dato, Tiempo):

        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)

            if val.is_displayed():
                val.send_keys(dato, Keys.ENTER, Keys.TAB)
                print("Insertamos {}" .format(dato))

                t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)

    ## Funcion Mouse Click
    def clic_xpath_valida(self, xpath, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)
            val.click()
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)

    ## Funcion Mouse doble click
    def double_clic_xpath(self, xpath, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)
            action = ActionChains(self.driver)
            action.double_click(val).perform()
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)

    def texto_ID_valida(self, ID, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("ID", ID)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("ID", ID)
            val.clear()
            print(texto)
            val.send_keys(texto)
            print("Escribiendo en el campo el texto {} ".format(texto))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + ID)


    def text_mixto(self, tipo, selector, texto, tiempo):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(tiempo)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif(tipo=="id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(tiempo)
                print("escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Upload_xpath_file(self, xpath, docs, tiempo=3):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)

            if val.is_displayed():
                val.send_keys("C://Users//cmhernandez//Desktop//Tramites//Deslinde//4000resultantes.xml")
                print("Insertamos ")
            #val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)



    def Mouse_DragDrop(self, tipo, selector, destino, tiempo=.2):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val2 = self.SEX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val2 = self.SEI(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
'''
    ''' def cargarDoc(self):
        if self.driver.find_element("xpath", "").is_displayed:
            print("Carga de archivo existosa")
        else:
            print("No se pudo cargar el archivo")
            
       for option in val:
        print(option.text + "== "+dato)
        if option.text == dato:
            break
        else:
            ARROW_DOWN = u'\ue015'
            val.send_keys(ARROW_DOWN)           
       '''