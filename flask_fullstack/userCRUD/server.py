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
    User.create_user(form_info)
    return redirect('/')


# * VIEW ONE PAGE WE GRAB THE ID FROM THE TABLE THEN TYPE CAST IT TO AN INT IN OUR URL 
# * MAKE SURE TO ALSO PASS IT AS A PARAM TO OUR FUNCTION 
@app.route('/view/user/<int:id>')
def view_one_user(id):
    print(id)
    data_from_controller = {
        'user_id': id
    }
    return render_template('one_user.html', this_user = User.get_one(data_from_controller))

# * JUST LIKE NEW USER THIS ONLY RENDERS A PAGE WITH THE FORM TO EDIT THE USER WHICH IS HANDLED IN A DIFFERENT ROUTE USE THAT ID AGAIN TO GRAB THE USER WITH OUR GET ONE CALL WE ALREADY WROTE 
@app.route('/edit/user/<int:id>')
def edit_user(id):
    data_from_controller = {
        'user_id': id
    }
    return render_template('edit_user.html', this_user = User.get_one(data_from_controller))

# * AGAIN USING THE ID THIS TIME TO AVOID HIDDEN INPUTS 
@app.route('/update/user/<int:id>', methods=['POST'])
def update_user(id):
    # print(request.form['id'])
    print(id)
    # ! THIS TIME WE HAVE TO MAKE A CUSTOM DICTIONARY BECAUSE THE ID IS NOT COMING FROM THE FORM 
    data = {
        'f_name': request.form['f_name'],
        'l_name': request.form['l_name'],
        'email': request.form['email'],
        'id': id,
    }
    # * CALLING TO OUR DB
    User.update(data)
    return redirect('/')

# * DELETE USING ID AGAIN SINCE ITS UNIQUE! 
@app.route('/delete/user/<int:id>')
def delete_user(id):
    data={
        'id':id
    }
    User.delete(data)
    # * YOU CAN MAKE THE DICTIONARY IN THE () AS SHOWN BELOW DONT WORRY IF YOU DONT LIKE THIS ITS JUST ANOTHER APROACH BOTH WORK ALL THE SAME AND ARE MORE THAN ACCEPTABLE 
    # User.delete({
    #     'id':id
    # })
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)