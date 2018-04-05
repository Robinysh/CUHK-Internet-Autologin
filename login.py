from splinter.browser import Browser
from time import sleep
 
URL = 'https://securelogin.net.cuhk.edu.hk/upload/custom/CUPortal/login.html'
NAME = 's1155000000'
PASSWORD = 'password'
 
def main():
    #br = Browser('chrome', executable_path='./chromedriver')
    br = Browser('chrome', executable_path='./chromedriver', headless=True)
    #print('opened')
    br.visit(URL)
    #print('visted')
    sleep(1)
    br.fill('user', NAME)
    br.fill('password', PASSWORD)
    br.find_by_name('Login').first.click()
    sleep(3)
 
if __name__ == "__main__":
    main()
