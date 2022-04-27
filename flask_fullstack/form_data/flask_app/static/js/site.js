window.onload = () => {
    fetch('http://localhost:5000/users')
    .then(res =>  res.json())
    .then(data => {
        var users = document.getElementById('users');
        for( let i = 0; i < data.length; i++){
            let row = document.createElement('tr');

            let name = document.createElement('td');
            name.innerHTML = data[i].user_name;
            row.appendChild(name);
            
            let email = document.createElement('td');
            email.innerHTML = data[i].email;
            row.appendChild(email);
            users.appendChild(row);
        }
    })

}
var myForm = document.getElementById('myForm');
myForm.onsubmit = function(e){
    // "e" is the js event happening when we submit the form.
    // e.preventDefault() is a method that stops the default nature of javascript.
    e.preventDefault();
    // create FormData object from javascript and send it through a fetch post request.
    var form = new FormData(myForm);

    let err_box = document.getElementById("err")
    err_box.innerHTML = "";

    let n = form.get("user_name")
    let em = form.get("email")


    if(n.length < 2){
        let err = document.createElement("p")
        err.innerHTML = "User name must be more than 2 characters"
        err.style.fontSize = "x-large"
        err.classList.add("text-danger")
        err_box.append(err)
    }
    if(em.length < 3){
        let err = document.createElement("p")
        err.innerHTML = "Email must be more than 3 characters!"
        err.style.fontSize = "x-large"
        err.classList.add("text-danger")
        err_box.append(err)
    }
    else{
        // this how we set up a post request and send the form data.
        fetch("http://localhost:5000/add_user", { method :'POST', body : form})
            .then( (response) => {
                console.log(response)
                response.json() 
                })
            .then(() => {
                let row = document.createElement('tr');
    
                let name = document.createElement('td');
                    name.innerHTML = n;
                    row.appendChild(name);
                    
                let email = document.createElement('td');
                    email.innerHTML = em;
                    row.appendChild(email);
                    users.appendChild(row);
            })
        myForm.reset()

    }
}

