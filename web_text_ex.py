from selenium import webdriver

browser=webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem=browser.find_element_by_css_selector('.entry-content > p:nth-child(4)')
print(elem.text)


#elem=browser.find_element_by_css_selector('html')
#print(elem.text)

browser.close()
