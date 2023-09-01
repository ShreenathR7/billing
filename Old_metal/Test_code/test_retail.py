# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key,Controller
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_Estimation(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(8)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Estimation).click()
        sleep(15)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Add_Estimation).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys('Head OFFICE')
        branch.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN) 
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Customer)
        sleep(10)
        customer.send_keys('KANNAN')
        sleep(5)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        print('Total',len(se_ver))
        customer_name = 'KANNAN -8989854215'
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Close).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().old_metal).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Metals).click()
        sleep(5)
        metals = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        metals.send_keys('Gold')
        metals.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Metals_Type).click()
        sleep(5)
        Metals_Type = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Metals_Type.send_keys('BEATEN GOLD')
        Metals_Type.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Category).click()
        sleep(5)
        Category = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Category.send_keys('GOLD COIN')
        Category.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().purity_metal).send_keys(data.Logi_Data().purity_value)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().metal_G_wt).send_keys(data.Logi_Data().G_wt_value)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().metal_D_wt).send_keys(data.Logi_Data().Dust_wt)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().metal_wastage_percentage).send_keys(data.Logi_Data().non_wastage_per)
        sleep(20)
        '''self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purpose).click()
        sleep(5)
        purpose_list = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        purpose_list.send_keys('Cash')
        purpose_list.send_keys(Keys.RETURN) '''
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Remark).send_keys(data.Logi_Data().remarks)   
        sleep(15)     
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_print).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation old metal  completed successfully,     metals : {a}, Metals_Type : {b}, Category : {c}, purity : {d}, metal_G_wt : {e}, metal_D_wt : {f}, metal_wastage_percentage : {g},".format(a= 'Gold', b='BEATEN GOLD', c='GOLD COIN', d = data.Logi_Data().purity_value, e =data.Logi_Data().G_wt_value, f = data.Logi_Data().Dust_wt, g = data.Logi_Data().non_wastage_per, ))
        
       
        
        
        
        
        
        
        
 