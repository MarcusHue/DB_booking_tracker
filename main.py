import scraper as scp
from database_handler import push_results_into_db
journey = {'origin':'Hamburg','destination': 'Osnabrück'}


data = scp.retrieve_data(journey = journey)

push_results_into_db(data)