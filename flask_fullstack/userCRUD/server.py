from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = "Friday I'm in love"

@app.route('/')
def index():
    return render_template('index.html', all_users = User.get_all())

@app.route('/new/user')
def new_user():
    return render_template('new_user_form.html')

@app.route('/create/user', methods=["POST"])
def create_user():
    form_info = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email']
    }
    print(request.form)
    print(form_info)
    User.create_user(form_info)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)