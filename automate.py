
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as sl
import getpass

import datetime
from datetime import date, timedelta
import os, os.path


def SendReportFile():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options,executable_path=r"D:\\Reporting Python\\chromedriver.exe")
    wait = WebDriverWait(driver, 600)

    with open('D:\\Report Automation\\Mail Recipient List\\MTN Mail List\\PM_Checklist_send.txt','r') as credentials:
        details = credentials.readlines()
        mail_to,mail_cc,counter = details[0].strip(),details[1].strip(),int(details[2].strip())
    

    # mailSubj = 'Airtel Health Check Report for' + file_date
    mailSubj = 'PM REPORT FOR Active Routine Maintenance/MTN Enterprise Link'
    now = datetime.now()
    nownow = now.strftime("%d-%m-%y")
    at  = r"D:\\Report Automation\\MTN Report Automation\\PM PDF Auto\\Input File\\checklist_export_report" + now +".zip"
    mailContent = 'Dears,'+'\n\n'+'Please see attached Report of completed PM Task'+'\n\n\n\n'+'Regards'+'\n'+'Huawei Enterprise NOC'+'\n\n\n'  
   

    with open('D:\\Report Automation\\Login_details\\SAR_AMS_OWS_login.txt','r') as credentials:
            details = credentials.readlines()
            username,password,counter = details[0].strip(),details[1].strip(),int(details[2].strip())


    driver.maximize_window()
    driver.get("https://15fg-saapp.teleows.com/app/15fg/spl/Report_Email_Receiver/email_send_create_v2.spl")
    sl.sleep(5)
    driver.refresh()
    sl.sleep(3)

    username_tag = 'usernameInput'
    x_arg = f'//input[contains(@id,"{username_tag}")]'
    usernameInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    usernameInput.send_keys(username)

    password_tag = 'password'
    x_arg = f'//input[contains(@id,"{password_tag}")]'
    usernameInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    usernameInput.send_keys(password)

    login = 'btn_submit'
    x_arg = f'//div[contains(@id,"{login}")]'
    loginBtn = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    loginBtn.click()
    print('login successful')
    sl.sleep(3)

    email_to = 'email_to'
    x_arg = f'//input[contains(@id,"{email_to}")]'
    emailToInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    emailToInput.send_keys(mail_to)

    email_cc = 'email_cc'
    x_arg = f'//input[contains(@id,"{email_cc}")]'
    emailCCInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    emailCCInput.send_keys(mail_cc)

    subject = 'title'
    x_arg = f'//input[contains(@id,"{subject}")]'
    usernameInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    usernameInput.send_keys(mailSubj)

    content_tag = 'content'
    x_arg = f'//textarea[contains(@id,"{content_tag}")]'
    contentInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    contentInput.send_keys(mailContent)

    attachment = '_uploadFile'
    x_arg = f'//form/input[contains(@name,"{attachment}")]'

    attachmentInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    print(attachmentInput)
    attachmentInput.send_keys(at)
    sl.sleep(5)
    
    sl.sleep(10) #file attachment delay
    
    #file_path_1_array = at.split('\\')
    #file_path_1_title = file_path_1_array[len(file_path_1_array) - 1].split('.')[0]
    #print(file_path_1_title)
    #x_arg = f'//div[contains(@class,"filelist_cls")]/a[contains(text(),"{attachment}")]'
    #attachmentInput = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
 
    submit = 'ServiceButton1'
    x_arg = f'//div[contains(@id,"{submit}")]'
    submitBtn = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    print("SUBMIT BUTTON CLICKED")
    submitBtn.click()
    

    sl.sleep(15)
    
    print("Mail Sending Completed...")
    driver.quit()
    


SendReportFile()
