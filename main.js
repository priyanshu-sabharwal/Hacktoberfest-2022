let cards = []
let sum
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.getElementById("sum-el")
let cardsEl = document.getElementById("cards-el")
let playerEl = document.getElementById("player-el")
let isFirstCard = true


function startGame(){
    if (isFirstCard === true){
    let firstCard = getRandomCard()
    let secondCard = getRandomCard()
    cards = [firstCard,secondCard]
    sum = firstCard + secondCard
    isFirstCard = false

    renderGame()
}
}

function renderGame(){
    sumEl.textContent ="Sum: " + sum
    if(sum < 21){
        message = "Do you want to draw a new card?"
    }
    else if(sum === 21){
        message = "You've got BlackJack"
        hasBlackJack = true
    }
    else{
        message = "You're out of the game!"
        isAlive = false
    }
    messageEl.textContent = message
    cardsEl.textContent = "Cards: " 
    for(let i=0 ;i< cards.length; i++){
        cardsEl.textContent += cards[i] +" "
    }
}
function newCard(){

    if (isAlive === true && hasBlackJack === false && isFirstCard === false){
    let nextCard = getRandomCard()
    cards.push(nextCard)
    sum += nextCard
    renderGame()
    }
}
function getRandomCard(){
    let randomNo = Math.floor(Math.random()*13)
    randomNo += 1
    if (randomNo === 1)
    return 11
    else if (randomNo > 10)
    return 10
    else 
    return randomNo

}
