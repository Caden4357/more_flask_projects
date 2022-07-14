console.log("JS loaded ok!");
var cardImg = document.querySelector("#poke-59");
var isFlipped = false;

function flipCard() {
    console.log("card flipping action");
    if(isFlipped) {
        cardImg.src = "imgs/cardback.png";
    } else {
        cardImg.src = "imgs/arcanine.jpg";
    }
    isFlipped = !isFlipped;
}

function hoverOver(ele) {
    ele.style.boxShadow = "8px 8px 8px #333";
}

function hoverOut(ele) {
    ele.style.boxShadow = "none";
}