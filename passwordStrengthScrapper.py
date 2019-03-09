from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webpage = r"https://www.cryptool.org/en/cto-highlights/passwordmeter"

driver = webdriver.Chrome('./chromedriver')
driver.get(webpage)
passwordInputElement = driver.find_element_by_class_name("form-control")

strengthPercentages = []
for i in range(1):
    filename = str(i) + ".txt"
    filepath = "./Dataset/Password List/" + filename
    with open(filepath) as f:
        start = 0
        for line in f:
            credentials = line.strip().split(':')
            j = 0
            for cred in credentials:
                if(j!= 0):
                    passwordInputElement.send_keys(cred)
                    strengthPercent = driver.find_element_by_class_name("results-text").text.split('%')[0]
                    strengthPercentages.append(strengthPercent)
                    passwordInputElement.clear()
                    j = 0 
                else:
                    j = 1

with open('passwordStrengths.txt', 'a+') as f:    
    for strengthPercentage in strengthPercentages:
        try:
            f.write("%s\n" % strengthPercentage)
        except IndexError:
            print ("A line in the file doesn't have enough entries.")