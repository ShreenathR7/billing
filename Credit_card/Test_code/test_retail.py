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
  
    
   
    def test_Billing(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Billing).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Bill).click()
        sleep(5)
        Branch = Select (self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Branch))
        Branch.select_by_value('1')
        selected_option = Branch.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Cost Centre name : {a}'.format(a = selected_text))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('billing Sales Employee name  : {a}'.format( a='111-Logimax Developer'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().sales).click()
        Sale_button = self.driver.find_element(By.XPATH, '(//*[@class="custom-label"])').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Billing to : {a}'.format( a= Sale_button))

        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Esti).send_keys(data.Logi_Data().Esti_No)    
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Estimation Number: {a}'.format(a = data.Logi_Data().Esti_No))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().close).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Total_summary).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().discount).clear
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().discount).send_keys(data.Logi_Data().Discount_amt)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Discount Amount (or) Round off : {a}'.format(a = data.Logi_Data().Discount_amt))
        sleep(5)
        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Make_payment).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().PAN_No).clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().PAN_No).send_keys(data.Logi_Data().PAN)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('PAN Number: {a}'.format(a = data.Logi_Data().PAN))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Adhaar_no).send_keys(data.Logi_Data().Adhaar)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Adhaar Number: {a}'.format(a = data.Logi_Data().Adhaar))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Driving_lic_No).send_keys(data.Logi_Data().Driving)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('drivng license Number: {a}'.format(a = data.Logi_Data().Driving))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Passport_no).send_keys(data.Logi_Data().Passport)  
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Passport Number: {a}'.format( a = data.Logi_Data().Passport))
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Tobe).click()
        Yes_button = self.driver.find_element(By.XPATH, '(//*[@for="is_to_be_yes"])').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Credit Option clicked : {a}'.format( a= Yes_button))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().credit_due_date).send_keys(data.Logi_Data().date)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Credit due date : {a}'.format(a = data.Logi_Data().date))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Received).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Received).send_keys(data.Logi_Data().amount)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Received Amount: {a}'.format(a = data.Logi_Data().amount))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Credit_card).click()      
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Add_credit_card).click()
        sleep(5)
        card = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_name))
        card.select_by_value('2')
        selected_option = card.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card Name : {a}'.format(a = selected_text))
        sleep(5)
        card_type = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_type))
        card_type.select_by_value('1')
        selected_option = card_type.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card type : {a}'.format(a = selected_text))
        sleep(5)
        card_device = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Device_name))
        card_device.select_by_value('1')
        selected_option = card_device.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Device Name : {a}'.format(a = selected_text))
        sleep(8)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_No).send_keys(data.Logi_Data().card_no)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card Number : {a}'.format(a = data.Logi_Data().card_no))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_amount).send_keys(data.Logi_Data().card_amount)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card Amount : {a}'.format(a = data.Logi_Data().card_amount))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().approval).send_keys(data.Logi_Data().approval_no)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Approval Number : {a}'.format(a = data.Logi_Data().approval_no))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().credit_pagr_save).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().billing_save).click()
        bill = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().billing_save).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation number : 5 Billing successfully completed payment ")
        
        
        
        