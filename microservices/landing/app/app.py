from flask import Flask, render_template, request, flash, redirect, url_for, make_response
import requests, requests.exceptions
import re
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'GET':
        flash('Enter Valid Input')

        
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')

    errors = False
    if number_1:
        if not re.match(r'^[+-]?\d+(\.\d+)?$', number_1):
            flash('Enter a valid input for number 1')
            errors = True

    if number_2:
        if not re.match(r'^[+-]?\d+(\.\d+)?$', number_2):
            flash('Enter a valid input for number 2')
            errors = True

    if number_1 is None:
        number_1 = '0'

    if number_2 is None:
        number_2 = '0'

    operation = request.form.get('operation')

    result = ""
    if not errors:
        try:
            if operation == 'add':
                result = requests.get('http://addition:5001/add/'+str(number_1) +'/'+str(number_2)).text
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}\n')
            elif operation == 'minus':
                result =  requests.get('http://subtraction:5002/sub/'+str(number_1) +'/'+str(number_2)).text
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}\n')
            elif operation == 'multiply':
                result = requests.get('http://multiplication:5003/mul/'+str(number_1) +'/'+str(number_2)).text
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}\n')
            elif operation == 'divide':
                result = requests.get('http://division:5004/div/'+str(number_1) +'/'+str(number_2)).text
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}\n')
                
            elif operation == 'gcd':
            	if number_1 and number_2:
            		if not re.match(r'^[-+]?\d+$', number_1) or not re.match(r'^[-+]?\d+$', number_2):
            			flash('Enter valid input for GCD operation. GCD accepts only positive, negative integers and 0')
            			errors = True
            		if not errors:
            			if int(number_1) < 0 and int(number_2) < 0:
            				result = requests.get('http://gcd:5005/gcd/'+str(number_1)+'/'+str(number_2)).text
            				result_temp = '-'+result
            				flash(f'The result of operation {operation} on {number_1} and {number_2} is {result_temp}\n')
            			else:
            				result = requests.get('http://gcd:5005/gcd/'+str(number_1)+'/'+str(number_2)).text
            				flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}\n')

            elif operation=='mod':
                result=requests.get('http://modulus:5006/mod/'+str(number_1) +'/'+str(number_2)).text
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}\n')
            elif operation=='equal':
                result=requests.get('http://equal:5007/equal/'+str(number_1) +'/'+str(number_2)).text
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}\n')
        except requests.exceptions.RequestException as e:
            result_error = f"Microservice {operation} is down"
            flash(f'{result_error}\n')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
