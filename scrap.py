from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/explore/tags/bitcoin')
soup = BeautifulSoup(driver.page_source, "lxml")
driver.quit()

for item in soup.select('._t98z6'):
    posts = item.select('._fd86t')[0].text
    print('Posts : {}'.format(posts))
