#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:16:20 2020

@author: janaingram
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class Google_Test(unittest.TestCase):
    
    def set_up(self):
        self.driver = webdriver.Chrome(executable_path='/users/janaingram/downloads/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    def test_search(self):
        self.driver = webdriver.Chrome(executable_path='/users/janaingram/downloads/chromedriver')
        self.driver.get("https://www.github.com/")
        self.driver.find_element_by_name('q').send_keys("jlingram1")
        self.driver.find_element_by_name("q").send_keys(Keys.RETURN)
      
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()

