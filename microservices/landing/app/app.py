from flask import Flask, render_template, request, flash, redirect, url_for
import requests, requests.exceptions
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        flash(f'Enter Valid Input')
        return render_template('index.html')
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    
    flag1 = 0
    flag2 = 0
    if number_1 is not None or number_2 is not None:
        if((number_1[0] == '-' and number_1[1:].isnumeric()) or (number_1.isnumeric())):
            flag1 =1
        if((number_2[0] == '-' and number_2[1:].isnumeric()) or (number_2.isnumeric())):
            flag2 =1

    operation = request.form.get('operation')
    if flag1 == 0 or flag2==0:
        flash(f'Enter Valid Input')
        return render_template('index.html')

    result = ""
    try:
        if operation == 'add':
            result = requests.get('http://addition:5001/add/'+str(number_1) +'/'+str(number_2)).text
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        elif operation == 'minus':
            result =  requests.get('http://subtraction:5002/sub/'+str(number_1) +'/'+str(number_2)).text
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        elif operation == 'multiply':
            result = requests.get('http://multiplication:5003/mul/'+str(number_1) +'/'+str(number_2)).text
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        elif operation == 'divide':
            result = requests.get('http://division:5004/div/'+str(number_1) +'/'+str(number_2)).text
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        elif operation=='gcd':
            result=requests.get('http://gcd:5005/gcd/'+str(number_1) +'/'+str(number_2)).text
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        elif operation=='mod':
            result=requests.get('http://modulus:5006/mod/'+str(number_1) +'/'+str(number_2)).text
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        elif operation=='equal':
            result=requests.get('http://equal:5007/equal/'+str(number_1) +'/'+str(number_2)).text
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    except requests.exceptions.RequestException as e:
        result_error = f"Microservice {operation} is down"
        flash(f'{result_error}')
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
