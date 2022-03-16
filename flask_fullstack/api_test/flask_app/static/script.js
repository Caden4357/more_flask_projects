const button = document.getElementById('button')

button.addEventListener('click', function(){
    fetch("http://www.boredapi.com/api/activity/")
    .then(response => response.json() )
    .then(coderData => document.getElementById('activity-text').innerText = coderData['activity'] )
    .catch(err => console.log(err) )
})