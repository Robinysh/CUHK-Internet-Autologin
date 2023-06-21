from splinter import Browser
from time import sleep
 
URL = 'https://securelogin.net.cuhk.edu.hk/'
ACCTNAME = '' # remember to change it to your CUHK email used for logging in WiFi
PASSWORD = '' # remember to change it to your own Onepass password
 
def main():
    #br = Browser('chrome', executable_path='./chromedriver')
    br = Browser('chrome')
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
