# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 05:08:06 2023

@author: pande
"""

import sqlite3

# Database file name
database = 'ambalika_database.db'

# Function to establish a database connection and create Company_detail table
def company_table_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ambalika_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_name TEXT,
            address TEXT,
            phone INTEGER,
            email TEXT,
            cin INTEGER,
            udyam INTEGER,
            pan TEXT,
            gstin_no TEXT
        )
        ''')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to establish a database connection and create Company_detail table
def client_bill_table_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS client_bill_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT,
            client_address TEXT,
            client_phone_no INTEGER,
            client_email TEXT,
            client_gstin INTEGER,
            place_of_supply TEXT,
            state_code INTEGER,
            tax_inv_date,
            date DATE,
            name_of_service TEXT,
            container_no INTEGER,
            size INTEGER,
            from_place TEXT,
            to_place TEXT,
            lr_no INTEGER,
            amount INTEGER,
            gst_amt INTEGER, 
            final_amount INTEGER
        )
        ''')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to insert data into the table
def writedata_company_details(database, business_name, address, phone, email, cin, udyam, pan, gstin_no):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        # Insert the data into the 'comp_Details' table
        cursor.execute('''
            INSERT INTO ambalika_details (business_name, address, phone, email, cin, udyam, pan, gstin_no)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (business_name, address, phone, email, cin, udyam, pan, gstin_no))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print(e)
        
 # Function to insert data into the table
def writedata_clientbill_details(database, client_name, client_address, client_phone_no, client_email, client_gstin, place_of_supply, state_code, tax_inv_date, date, name_of_service, container_no, size, from_place, to_place, lr_no, amount, gst_amt, final_amount, gst_per):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        # Insert the data into the 'comp_Details' table
        cursor.execute('''
            INSERT INTO client_bill_table (client_name, client_address, client_phone_no, client_email, client_gstin, place_of_supply, state_code, tax_inv_date, date, name_of_service, container_no, size, from_place, to_place, lr_no, amount, gst_amt, final_amount, gst_per)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (client_name, client_address, client_phone_no, client_email, client_gstin, place_of_supply, state_code, tax_inv_date, date, name_of_service, container_no, size, from_place, to_place, lr_no, amount, gst_amt, final_amount, gst_per))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print(e)
        
        
# Function to read data from the table within a date range
def read_ambalika_details(database):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM ambalika_details
        ''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
        
# Function to read data from the table within a date range
def readdata_clientbill_details(database):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM client_bill_table
        ''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)