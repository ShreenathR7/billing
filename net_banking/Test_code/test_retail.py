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
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().discount_amt).clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().discount_amt).send_keys(data.Logi_Data().discount)
        
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
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().net_banking).click()
        sleep(5)
        net_banking = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().net_banking_type))
        net_banking.select_by_value('2')
        selected_option = net_banking.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Net Bank type : {a}'.format(a = selected_text))
        sleep(5)
        net_bank = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().net_bank))
        net_bank.select_by_value('6')
        selected_option = net_bank.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Net Bank Name : {a}'.format(a = selected_text))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().payment_date).send_keys(data.Logi_Data().pay_date)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Payment Date : {a}'.format(a = data.Logi_Data().pay_date))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Referral_no).send_keys(data.Logi_Data().ref_no)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Referral Number: {a}'.format(a = data.Logi_Data().ref_no))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().net_banking_amount).send_keys(data.Logi_Data().net_bank_amount)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Net Banking Amount : {a}'.format(a = data.Logi_Data().net_bank_amount))
        sleep(5)                
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().net_bank_page_save).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().billing_save).click()
        #bill = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().billing_save).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation number : 1  Billing successfully completed Net banking payment")
        
        
        
        