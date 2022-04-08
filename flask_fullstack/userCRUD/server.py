from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = "Friday I'm in love"


# * ROOT ROUTE RENDERS INDEX.HTML WHICH HAS A TABLE THAT DISPLAYS ALL USERS IN DB COMING FROM CALL USER.GETALL()
@app.route('/')
def index():
    return render_template('index.html', all_users = User.get_all())


# * ONLY RENDERS AN HTML PAGE THAT HAS A FORM TO CREATE A NEW USER 
@app.route('/new/user')
def new_user():
    return render_template('new_user_form.html')


# * PROCESSES THE POST REQUEST TO CREATE THE USER 
@app.route('/create/user', methods=["POST"])
def create_user():
    # *CREATING OUR OWN FORM DICTIONARY TO BETTER CONTROL THE DATA BEING SENT TO OUR QUERY 
    form_info = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email']
    }

    # ? LOOK AT WHAT PRINTS OUT REQUEST.FORM IS A DICTIONARY SPECIFICALLY A IMMUTABLEMULTIDICT WHICH IS A SUBCLASS OF A DICTIONARY 
    print(request.form)
    print(form_info)

    # * MAKING A CALL TO OUT DB SENDING IN OUR DICTIONARY TO INSERT A NEW USER INTO TABLE USERS 
    this_users_id = User.create_user(form_info)
    print(this_users_id)
    return redirect(f'/view/user/{this_users_id}')

@app.route('/view/user/<int:id>')
def view_one_user(id):
    # print(id)
    data = {
        'id': id
    }
    # print(data)
    this_user = User.view_one(data)
    return render_template('view_one.html', user=this_user)

@app.route('/edit/user/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    # print(data)
    this_user = User.view_one(data)
    return render_template('edit_user.html', user=this_user)

# route for editing user coming soon
@app.route('/update/user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    form_info = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email'],
        'id':user_id
    }
    # print(form_info)
    User.update_user(form_info)
    return redirect('/')

@app.route('/delete/user/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


