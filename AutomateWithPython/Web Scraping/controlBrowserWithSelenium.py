from selenium import webdriver as wd

browser = wd.Firefox()
browser.get('https://automatetheboringstuff.com/')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(24) > li:nth-child(1) > a')
print(elem)

elem.click()

elems = browser.find_element_by_css_selector('p')
print(len(elems))

searchElem = browser.find_element_by_css_selector('.search-field')

searchElem.send_keys('robocup')
searchElem.submit()

##browser.back()
##browser.forward()
##browser.refresh()
##browser.quit()

elem = browser.find_element_by_css_selector('#calibre_link-90 > div > p:nth-child(2)')
')

elem.text

elem = browser.find_element_by_css_selector('html') # copy all html elements
