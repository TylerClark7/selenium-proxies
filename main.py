from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#options = webdriver.ChromeOptions()


options = Options()
proxy_server_url ="67.43.227.229:29003"
options.add_argument(f'--proxy-server={proxy_server_url}')
driver = webdriver.Chrome(options=options)

driver.get("https://whatismyipaddress.com/")
driver.implicitly_wait(8)
ip_address = driver.find_element(By.ID, 'ipv4').text

driver.close()

print(ip_address)

