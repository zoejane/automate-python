from selenium import webdriver



browser=webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
elem=browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')
elem.click()
#elems=browser.find_elements_by_css_selector('p')
#print(len(elems))


elem=browser.find_element_by_css_selector('.fa-align-right')
elem.click()

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()
