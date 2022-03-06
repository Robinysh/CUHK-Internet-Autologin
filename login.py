from splinter.browser import Browser
from time import sleep
 
URL = 'https://securelogin.wlan.cuhk.edu.hk/'
ACCTNAME = ''
PASSWORD = '' #remember to change it to your own Onepass password
 
def main():
    #br = Browser('chrome', executable_path='./chromedriver')
    br = Browser('chrome', executable_path='./chromedriver', headless=True)
    print('opened')
    br.visit(URL)
    print('visited')
    sleep(5)
    br.find_by_xpath('//input[@type="checkbox"]').first.click()
    br.find_by_name('accept').first.click()
    print('accept terms')
    sleep(5)
    br.fill('user', ACCTNAME)
    br.fill('password', PASSWORD)
    br.find_by_name('submit').first.click()
    sleep(3)
 
if __name__ == "__main__":
    main()
