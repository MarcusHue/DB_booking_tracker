import scraper as scp
from database_handler import push_results_into_db

data = scp.retrieve_data()

push_results_into_db(data)