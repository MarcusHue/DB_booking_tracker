#############################################
# This file contains all functions that are #
# required for handling the database        #
#############################################


import mysql.connector
import pandas as pd
from mysql.connector import Error
from mysql.connector import errorcode
from config import sql_config
import ast 

# Function that will take any querry for pushing into the db and send it
def execute_push_sql(querry):
  try:
      connection = mysql.connector.connect(**sql_config)
      cursor = connection.cursor()
      result  = cursor.execute(querry)
      connection.commit()
      print ("Executed querry")
  except mysql.connector.Error as error :
      connection.rollback() #rollback if any exception occured
      print("Failed executing querry {}".format(error))
  finally:
      #closing database connection.
      if(connection.is_connected()):
          cursor.close()
          connection.close()
          print("MySQL connection is closed")


# Function that takes the result dictionary and pushes the values into the raw_data db
def push_results_into_db(result):
  querry = "INSERT INTO raw_data (arrival_time_planned, arrival_time_actual, departure_time_planned, departure_time_actual, utalisation, train_number) VALUES ('{timestamp}','{url}',{number_comments}, '{error}')".format(
        timestamp = result.get('timestamp'), 
        url = result.get('url'), 
        number_comments = result.get('number_comments'),
        error = result.get('error'))
  execute_push_sql(querry)


