
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
#print(type(browser))
browser.get('https://www.moneycontrol.com/india/stockpricequote/')

#try:
#emailElem = browser.find_element_by_id("txtemail")
#passwordElem = browser.find_element_by_id("txtpassword")
#loginbtnElem = browser.find_element_by_id("btnlogin")
searchElem = browser.find_element_by_id('search_str')
#htmlElem = browser.find_element_by_tag_name("html")
#print(f'Found {emailElem.tag_name}, {passwordElem.tag_name} and \
#{loginbtnElem.tag_name}')
#elem.click()
#emailElem.send_keys('cma.ankitgupta84@gmail.com')
#passwordElem.send_keys('ankcapri20')
#loginbtnElem.click()
#htmlElem.send_keys(Keys.END)
#htmlElem.send_keys(Keys.HOME)
searchElem.send_keys('Bajaj Finance')
searchElem.send_keys(Keys.ENTER)
#emailElem.submit()
input('Want to quit ?')
browser.quit()
print('Done')
    
#except Exception as ex:
#    print('Exception is: ',ex)
