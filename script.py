def firefox_driver():
    #Going to use Selenium to take screenshot of a given url using firefox driver

    from selenium import webdriver
    from time import sleep

    url = "http://www.outlook.com"                      # the url that we give

    driver = webdriver.Firefox(executable_path=r'/home/alidotm/Desktop/freelance_work/singapore/geckodriver')   # the path to the web driver
    
    driver.get('http://www.google.com/')                                

    search_box = driver.find_element_by_name('q')
    search_box.send_keys(url)
    search_box.submit()

    #time.sleep(3) 
    
    driver.get(url)                                          # opens the website to get screenshot

    driver.get_screenshot_as_file("screenshot_fire.png")             # screenshot taken
    driver.quit()                                             
    print("Screenshot taken and saved in your folder!")
    
    # Now going to also print Title of website after taking screenshot using Beautiful Soup!

    import requests
    from bs4 import BeautifulSoup

    # making requests instance
    reqs = requests.get(url)                                          # the same url we gave is requested

    # using the BeaitifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')

    # displaying the title
    print("Title of the website is : ")
    for title in soup.find_all('title'):
        a = title.get_text()
        a = a.strip('\n')
        print(title.get_text())
        
def chrome_driver():
    #Going to use Selenium to take screenshot of a given url using chrome driver
    
    import time
    from selenium import webdriver
    
    url = "http://www.outlook.com"                 # the url it will search

    driver = webdriver.Chrome('/home/alidotm/Desktop/freelance_work/singapore/chromedriver')  # Optional argument, if not specified will search path.
    
    driver.get('http://www.google.com/')                                

    search_box = driver.find_element_by_name('q')
    search_box.send_keys(url)
    search_box.submit()

    time.sleep(3)                             # Enough time to see it going
    
    driver.get(url)                                       
    driver.get_screenshot_as_file("screenshot_chrome.png")         # for screenshot capturing

    driver.quit()
    print("Screenshot taken and saved in your folder!")
    
    # Now going to also print Title of website after taking screenshot using Beautiful Soup!

    import requests
    from bs4 import BeautifulSoup

    # making requests instance
    reqs = requests.get(url)                                          # the same url we gave is requested

    # using the BeaitifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')

    # displaying the title
    print("Title of the website is : ")
    for title in soup.find_all('title'):
        a = title.get_text()
        a = a.strip('\n')
        print(title.get_text())
        
def start():
    driver_choice = input("For Chrome Driver: Press '1'\nFor Firefox Driver: Press '2'\n")
    if driver_choice == '1':
        chrome_driver()
    elif driver_choice == '2':
        firefox_driver()
    else:
        print('You did not enter correct format. Try again.')
        
start()
