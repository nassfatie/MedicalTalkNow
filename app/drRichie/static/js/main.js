const submitButton = document.querySelector('#submit');
const botOutput = document.querySelector('#output');
const userInput = document.querySelector('input');
const chatHistory = document.querySelector('.history');
const newChat = document.querySelector('.chat_button');

function chnageInput(value){
    const inputElement = document.querySelector('input');
    inputElement.value = value

};

async function getmessage(){
    console.log('clicked');
    const options = {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        mode: 'cors',
        body: JSON.stringify({ content: userInput.value }),
    };
    try{
        const response = await fetch('http://127.0.0.1:5000/app/chat', options);
        const data = await response.json();
        console.log(data);
        botOutput.textContent = data.answer;
        if (data.answer){
            const pElement = document.createElement('p');
            pElement.textContent = userInput.value;
            pElement.addEventListener('click', ( ) => chnageInput(pElement.textContent))
            chatHistory.append(pElement);
        }

    } catch (error){
        console.error(error);
    }
};
submitButton.addEventListener('click', getmessage);
function clearInput(){
    userInput.value = '';
};
newChat.addEventListener("click", clearInput);