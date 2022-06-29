from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
import os
import sys

path = sys.argv[1]
print(path)
with open(path) as f:
	data=f.read()

data = data.split('\n')[:-1]

myuser=data[0]
mypass=data[1]
mysec=[data[3],data[5],data[7]];

path=os.path;
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install());
driver.maximize_window();
driver.get("https://erp.iitkgp.ac.in/")
driver.implicitly_wait(6)
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[1]/input").send_keys(myuser)
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[2]/input").send_keys(mypass)
lab=WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[3]/label")))
ques=lab.text
answer=WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[3]/input")))
if ques==data[2]:
	answer.send_keys(mysec[0])
elif ques==data[4]:
	answer.send_keys(mysec[1])
else:
	answer.send_keys(mysec[2])
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[4]/div/input[3]").click()
