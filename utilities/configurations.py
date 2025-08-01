# Created by Satvik Jayalwal
# Utility module to handle MySQL connections and queries using configuration from .ini file

import configparser  # For reading configuration settings
import mysql.connector  # MySQL client library
from mysql.connector import Error  # For catching MySQL-related errors


# Function to read SQL configuration details from properties.ini
def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\python_codes\\BackEndAutomation\\utilities\\properties.ini')
    return config


# Dictionary to hold MySQL connection configuration
connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
}


# Returns a hardcoded password (can be replaced with secure retrieval method)
def getPassword():
    return "Srinath19830G"  # Consider moving this to environment variables for security


# Function to establish a connection to MySQL using config values
def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print("Connection failed:", e)


# Function to execute a SELECT query and return the first row of result
def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()  # Fetch only one row from result set
    conn.close()
    return row
