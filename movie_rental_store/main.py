"""Main"""
import sys
import os
sys.path.append(os.path.abspath("src"))

from configure import CSV_CUSTOMERS_PATH
from modules.handler.manage_customer import ManageCustomer
from modules.handler.import_customer import ImportCustomer

if __name__ == "__main__":
 
  # Get data for customer from console
  print "Register a customer using console"
  customer_handler = ManageCustomer("customer_001")
  customer_handler.read_first_name()
  customer_handler.read_last_name()
  customer_handler.read_date_of_birth()
  customer_handler.read_addresses()
  customer_handler.read_phones()
  customer_handler.read_membership()
  customer_handler.read_status()
  
  # import customers from csv file
  print "Import customer from csv files"
  customer_csv_file = ImportCustomer()
  customer_csv_file.import_customer_csv_file(CSV_CUSTOMERS_PATH)