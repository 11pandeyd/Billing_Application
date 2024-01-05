from flask import Flask, render_template, request, redirect, url_for
import db_code
import bill_code
import db_code

app = Flask(__name__)

# Database file name
database = 'ambalika_database.db'

# Function to initialize the database tables
def initialize_database():
    db_code.company_table_connection(database)
    db_code.client_bill_table_connection(database)

# Home route
@app.route('/')
def show_form():
    return render_template('billing_form.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    try:
        # Client details
        client_name = request.form['client_name'] 
        client_address = request.form['client_address']
        client_phone_no = request.form['client_phone_no'] 
        client_email = request.form['client_email'] 
        client_gstin = request.form['client_gstin'] 
        place_of_supply = request.form['place_of_supply']
        state_code = int(request.form['state_code'])
        tax_inv_date = bill_code.get_todays_date()
        
        #Billing details
        name_of_service=request.form['name_of_service'] 
        container_no=request.form['container_no']
        size=request.form['size'] 
        from_place = request.form['from_place'] 
        to_place = request.form['to_place'] 
        lr_no = request.form['lr_no']
        amount = int(request.form['amount'])
        gst_per = int(request.form['gst_per'])
        
        #Getting todays date
        date = bill_code.get_todays_date()
        
        # GST calculation method called
        gst_amt, final_amount = bill_code.gst_calculation(gst_per, amount)
                       
        # Writing to DB
        db_code.writedata_clientbill_details(database, client_name, client_address, client_phone_no, client_email, client_gstin, place_of_supply, state_code, tax_inv_date, 
                                             date, name_of_service, container_no, size, from_place, to_place, lr_no, amount, gst_amt, final_amount, gst_per)

        # Render the output on a new page
        return render_template('billing_result.html', 
                               client_name = client_name, client_address = client_address, client_phone_no = client_phone_no, client_email = client_email, client_gstin = client_gstin, place_of_supply = place_of_supply, state_code = state_code, 
                               date = date, name_of_service = name_of_service, container_no = container_no, size = size, from_place = from_place, to_place = to_place, lr_no = lr_no, amount = amount, gst_amt = gst_amt, final_amount = final_amount, gst_per = gst_per
                               )
    except Exception as e:
        return f'Exception occurred: {str(e)}'


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
