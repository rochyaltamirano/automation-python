from re import search
from selenium import webdriver
import unittest

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('/Users/rocioaltamirano/automation-python/chromedriver')
driver.get('http://automationpractice.com/index.php')

search_box = driver.find_element_by_id('search_query_top')
search_box.send_keys('hola')

search_button = driver.find_element_by_name('submit_search')
search_button.click()

results_label = driver.find_element_by_xpath('//*[@id="center_column"]/p')

tc.assertEqual('No results were found for your search "hola"', results_label.text)

#

women_link = driver.find_element_by_link_text('Women')
women_link.click()


dress_link = driver.find_element_by_partial_link_text('Dres')
dress_link.click()

driver.close()
driver.quit()