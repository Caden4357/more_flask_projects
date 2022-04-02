from flask import Flask, render_template, redirect, request, session 
app = Flask(__name__) 
app.secret_key = "blah"
import random
from datetime import datetime


@app.route('/')          
def index():
    if 'gold' and 'activities' not in session:
        session['gold'] = 0
        session['activities'] = ""
    return render_template('index.html') 

@app.route('/process_money', methods=['POST'])
def process_gold():
    location = request.form['building']
    current_time = datetime.now().strftime(("%m/%d/%Y, %I:%M:%S %p"))
    print(current_time)
    if location == "farm":
        gold_this_turn = random.randint(10, 20)
        # print(gold_this_turn)
    elif location == "cave":
        gold_this_turn = random.randint(5, 10)
    elif location == "house":
        gold_this_turn = random.randint(2, 5)
    else:
        gold_this_turn = random.randint(-50,50)
    session['gold'] += gold_this_turn
    if gold_this_turn < 0:
        message = f"<p class='text-danger'>Oh no you entered the casino and lost {gold_this_turn} {current_time}</p>"
    else:
        message = f"<p class='text-success'>Earned {gold_this_turn} golds from {location} {current_time}</p>"
    session['activities'] += message
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":       
    app.run(debug=True)   

