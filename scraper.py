from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
import config
import utils
from scrapy import Selector

dirpath = os.getcwd()
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path = dirpath + '/geckodriver',options = options)
driver.get(config.url)



 
def type_in_origin(driver, origin):
    form_origin = driver.find_element_by_id(config.origin_field)
    form_origin.send_keys(origin)

def type_in_destination(driver, destination):
    form_destination = driver.find_element_by_id(config.destination_field)
    form_destination.send_keys(destination)

def navigate_to_result_page():
    driver = webdriver.Firefox(executable_path = dirpath + '/geckodriver',options = options)
    driver.get(config.url)
    type_in_origin(driver, config.origin)
    type_in_destination(driver, config.destination)
    btn_submit = driver.find_element_by_class_name(config.submit_button_class)
    btn_submit.click()
    btn_show_details = driver.find_element_by_id(config.details_button_id)
    btn_show_details.click()
    return(driver)


def retrieve_utilisation(driver):
    utilisation_element = driver.find_element_by_xpath(config.xpath_utilisation)
    utilisation = utilisation_element.get_attribute("title")
    return(utilisation)

def retrieve_departure_time(driver):
    time_element = driver.find_element_by_xpath(config.xpath_departure_time)
    time = time_element.text
    time = utils.clean_convert_time(time)
    return(time)

def retrieve_arrival_time(driver):
    time_element = driver.find_element_by_xpath(config.xpath_arrival_time)
    time = time_element.text
    time = utils.clean_convert_time(time)
    return(time)

def retrieve_product(driver):
    element = driver.find_element_by_xpath(config.xpath_product)
    product = element.text
    return(product)

def retrieve_data():
    driver = navigate_to_result_page()
    utilisation = retrieve_utilisation(driver)
    arrival_time = retrieve_arrival_time(driver)
    departure_time = retrieve_departure_time(driver)
    product = retrieve_product(driver)
    train_data = {  'arrival_time_planned'  :   arrival_time['planned_time'], 
                    'arrival_time_actual'   :   arrival_time['actual_time'], 
                    'departure_time_planned':   departure_time['planned_time'], 
                    'departure_time_actual' :   departure_time['actual_time'],
                    'utilisation'           :   utilisation ,
                    'product'               :   product
                    }
    driver.quit()
    return(train_data)



