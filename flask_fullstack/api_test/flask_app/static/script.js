const button = document.getElementById('button')

button.addEventListener('click', function(){
    let answer_div = document.getElementById("answer")
    fetch("http://www.boredapi.com/api/activity/")
    .then(response => response.json() )
    .then((data) => {
        document.getElementById('activity-text').innerText = data['activity'] 
        let btn = document.createElement("button")
        btn.innerHTML = "Add to your todo list"
        answer_div.appendChild(btn)
    })
    .catch(err => console.log(err) )
})