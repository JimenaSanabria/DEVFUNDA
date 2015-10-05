__author__ = 'JimenaSanabria'

import sys
import os
sys.path.append('../../src')
sys.path.append(os.path.abspath("../../"))

import datetime
from logs.logger_handler import LoggerHandler
from configure import DEFAULT_LOG_PATH

"""Method to validate input data from console."""

LOGGER = LoggerHandler(DEFAULT_LOG_PATH)

def get_date_input(item_name):
    """Verify that the input from console is a date.
    
    Keyword arguments:
    item_name -- the str with the name of item to be register as date

    Return the date regiter by console
    
    """ 

    while True:
        try:
            item = raw_input(item_name + " (dd-mm-yyyy):")
            item = datetime.datetime.strptime(item, "%d-%m-%Y")
            break
        except:
            LOGGER.error("Error, value: " + item +". It needs to have the format dd-mm-yyyy.")
    return item

def get_integer_input(item_name):
    """Verify that the input from console is an integer.
    
    Keyword arguments:
    item_name -- the str with the name of item to be register as integer
    
    Return the integer number register by console
    
    """

    while True:
        try:
            item = int(input(item_name + ":"))
            break
        except:
            LOGGER.error("Error, a " + item_name +" needs to be an integer number.")
    return item
    
def get_option_input(item_name, options_list):
    """Verify that the input from console is an option of list.

    Keyword arguments:
    item_name -- the str with the name of item to be register as option of list
    options_list -- the list of str with the the option of item_name
    
    Return the option of options_list register by console
    
    """

    while True:
        item = raw_input(item_name + ":")
        if item in options_list:
            break
        else:
            LOGGER.error("Error, value: " + item + ". " + item_name +" needs to be an option of list.")
    return item
