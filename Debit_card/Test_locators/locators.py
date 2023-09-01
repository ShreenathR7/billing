# locators.py - File where all The HTML Locators are Kept
class Logi_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '(//*[@role="button"])'
    
   
    Billing = '(//*[@class="fa fa-cc text-orange"])[2]'
    
    Bill  = '(//*[@class="fa fa-circle-o"])[100]'
    
    Branch = 'id_branch'
    
    text_box = '(//*[@role="textbox"])'
    
    Sales_Employee = 'select2-emp_select-container'
    
    sales = 'bill_typesales'
    
    Esti = 'filter_est_no'
    
    search = 'search_est_no'
    
    close = '(//*[@class="btn btn-warning"])[16]'
    
    Total_summary = 'tab_tot_summary'
    
    discount = 'summary_discount_amt'
    
    Make_payment = 'tab_make_pay'
    
    PAN_No = 'pan_no'
    
    Adhaar_no = 'aadhar_no'
    
    Driving_lic_No = 'dl_no'
    
    Passport_no = 'pp_no'
    
    Tobe = 'is_to_be_yes'
    
    Received = 'billing[tot_amt_received]'
    
    credit_due_date = 'credit_due_date'
    
    Cash = 'make_pay_cash'
    
    debit_card = 'card_detail_modal'
    
    Add_debit_card = 'new_card'
    
    card_name = 'card_details[card_name][]'
    
    card_type = 'card_details[card_type][]'
    
    Device_name = 'card_details[id_device][]'
    
    card_No = 'card_details[card_no][]'
    
    card_amount = 'card_details[card_amt][]'
    
    approval = 'card_details[ref_no][]'
    
    credit_pagr_save = 'add_newcc'
   
    billing_save = 'pay_submit'