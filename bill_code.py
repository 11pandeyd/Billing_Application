# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 05:08:03 2023

@author: pande
"""
from datetime import date 
import pandas as pd
import db_code

# Database file name
database = 'ambalika_database.db'

def get_todays_date():
    try:
        today = str(date.today())
    except:
        return 'error in get_todays_date method'
    return today

def ambalika_details():
    # business_name, address, phone, email, cin, udyam, pan, gstin_no
    try:
        business_name = str(input())
        address = str(input())
        phone = int(input())
        email = str(input())
        cin = int(input())
        udyam = int(input())
        pan = int(input())
        gstin_no = input()
        
        # Writing to Database
        db_code.writedata_company_details(database, business_name, address, phone, email, cin, udyam, pan, gstin_no)
        
        
    except:
        return 'error occured in comp_Details method'
    return business_name, address, phone, email, cin, udyam, pan, gstin_no

def client_details():
    try:
        client_name = str(input())
        client_address = str(input())
        client_phone_no = int(input())
        client_email = str(input())
        client_gstin = input()
        place_of_supply = input()
        state_code = input()
        tax_inv_date = get_todays_date()
    except:
        return 'error occcured in client_details method'
    return client_name, client_address, client_phone_no, client_email, client_gstin, place_of_supply, state_code, tax_inv_date

def invoice_body():
    try:
        date = get_todays_date()
        name_of_service = str(input())
        vechile_no = input()
        container_no = input()
        size = input()
        from_place = input()
        to_place = input()
        lr_no = input()
        amount = float(input())
    except:
        return 'exception occured in invoice_body method'
    return date, name_of_service, container_no, size, from_place, to_place, lr_no, amount


def gst_calculation(input_gst_perc,total_amount):
    try:
        gst_amt = (total_amount*input_gst_perc)/100.0
        final_amount = total_amount + gst_amt
    except:
        return 'exception occured in gst_calculation method'
    return gst_amt, final_amount


def final_billing_creation():
    try:
        client_name, client_address, client_phone_no, client_email, client_gstin, place_of_supply, state_code, tax_inv_date = client_details()
        date, name_of_service, container_no, size, from_place, to_place, lr_no, amount = invoice_body()
        gst_amt, final_amount = gst_calculation()

        #Writing to DB
        db_code.writedata_clientbill_details(database, client_name, client_address, client_phone_no, client_email, client_gstin, place_of_supply, state_code, tax_inv_date, date, name_of_service, container_no, size, from_place, to_place, lr_no, amount, gst_amt, final_amount)
    except:
        return 'exception occured in final_billing_creation'
    return date, name_of_service, container_no, size, from_place, to_place, lr_no, amount, gst_amt, final_amount
    
