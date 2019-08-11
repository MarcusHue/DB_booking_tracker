#database
sql_config = {'host':'localhost', 'database':'DB_scraper', 'user':'scraper', 'password':'scraper'}


#route

origin = 'Hamburg'
destination = 'Osnabrück'

#website
url = 'https://www.bahn.de'
origin_field = 'js-auskunft-autocomplete-from'
destination_field = 'js-auskunft-autocomplete-to'
submit_button_class = 'js-submit-btn'
details_button_id = 'linkDtlC0-0'
xpath_utilisation = '//tbody[2]/tr/td[@class="center lastrow"]/img[1]'
xpath_departure_time = '//tbody[2]/tr[1]/td[2]'
xpath_arrival_time_same_day = '//tbody[2]/tr[2]/td[2]'
xpath_arrival_time_next_day = '//tbody[2]/tr[3]/td[2]'
xpath_train_number =  '//tbody/tr[2]/td[4]/span'
