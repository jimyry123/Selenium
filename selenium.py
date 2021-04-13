from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import re

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path=r'C:/Users/jry158538/OneDrive - Applied Materials/Desktop/chromedriver/chromedriver.exe', desired_capabilities=chromeOptions.to_capabilities())
driver.get("http://spcustomapps/sites/PCRBCS/pcr/Lists/PCRList/AllItems.aspx")

bs_obj = BeautifulSoup(driver.page_source, 'html.parser')
rows = bs_obj.find_all('table')[0].find('tbody').find_all('tr')

states = []

for row in rows:
    cells = row.find_all('td', {'class':'ms-vb-title'})
    name = cells[0].get_text()
    name1 = cells[1].get_text()
    states.append([
         name,name1
    ])
    
print(states)


time.sleep(10)
driver.close()

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import re

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path=r'C:/Users/jry158538/OneDrive - Applied Materials/Desktop/chromedriver/chromedriver.exe', desired_capabilities=chromeOptions.to_capabilities())
driver.get("http://spcustomapps/sites/PCRBCS/pcr/Lists/PCRList/AllItems.aspx")

bs_obj = BeautifulSoup(driver.page_source, 'lxml')
rows = bs_obj.find('tbody').find('tr',{'class':'ms-itmhover'})
new_data = []
for data in bs_obj.find_all('td')[1:].contents:
    new_data.append([data])
    
df = pd.DataFrame(new_data)

print(df)

time.sleep(10)
driver.close()

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path=r'C:/Users/jry158538/OneDrive - Applied Materials/Desktop/chromedriver/chromedriver.exe', desired_capabilities=chromeOptions.to_capabilities())
driver.get("http://spcustomapps/sites/PCRBCS/pcr/Lists/PCRList/AllItems.aspx")

bs_obj = BeautifulSoup(driver.page_source, 'lxml')
table_body = bs_obj.find_all('tbody')[1]
rows = table_body.find_all('tr')
new_data = []
for data in rows:
    cols = data.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    
    new_data.append([ele for ele in cols if ele])
    
df = pd.DataFrame(new_data)

df1 = df.iloc[10:,0:110]

print(df.iloc[10:,0:10])

time.sleep(10)
driver.close()

