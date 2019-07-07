from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
import config
import utils
from scrapy import Selector

dirpath = os.getcwd()


options = Options()
options.headless = False


 
def type_in_origin(origin):
    form_origin = driver.find_element_by_id(config.origin_field)
    form_origin.send_keys(origin)

def type_in_destination(destination):
    form_destination = driver.find_element_by_id(config.destination_field)
    form_destination.send_keys(destination)

def navigate_to_result_page():
    type_in_origin(config.origin)
    type_in_destination(config.destination)
    btn_submit = driver.find_element_by_class_name(config.submit_button_class)
    btn_submit.click()
    btn_show_details = driver.find_element_by_id(config.details_button_id)
    btn_show_details.click()

def retrieve_utalisation():
    utalisation_element = driver.find_element_by_xpath(config.xpath_utalisation)
    utalisation = utalisation_element.get_attribute("title")
    return(utalisation)


def retrieve_departure_time():
    time_element = driver.find_element_by_xpath(config.xpath_departure_time)
    time = time_element.text
    time = utils.clean_convert_time(time)
    return(time)

def retrieve_arrival_time():
    time_element = driver.find_element_by_xpath(config.xpath_arrival_time)
    time = time_element.text
    time = utils.clean_convert_time(time)
    return(time)

def retrieve_data():
    navigate_to_result_page()
    utalisation = retrieve_departure_time()
    driver.quit()
    return(utalisation)

driver = webdriver.Firefox(executable_path = dirpath + '/geckodriver', options = options)
driver.get(config.url)
html = retrieve_data()

print(html)

