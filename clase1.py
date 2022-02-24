from selenium import webdriver
import unittest

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('/Users/rocioaltamirano/projects/automation/clase1/chromedriver')
driver.get('http://automationpractice.com/index.php')

driver.find_element_by_id('search_query_top').send_keys('hola')
driver.find_element_by_name('submit_search').click()

tc.assertEqual('No results were found for your search "hola"', driver.find_element_by_xpath('//*[@id="center_column"]/p').text)

driver.close()
driver.quit()