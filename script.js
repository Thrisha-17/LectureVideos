const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const notesArea = document.getElementById("notes");

let recognition;

if ('webkitSpeechRecognition' in window) {

recognition = new webkitSpeechRecognition();

recognition.continuous = true;
recognition.interimResults = true;

recognition.onresult = function(event) {

let transcript = "";

for (let i = event.resultIndex; i < event.results.length; i++) {

transcript += event.results[i][0].transcript;
}

notesArea.value = transcript;
};
}

startBtn.onclick = () => {
recognition.start();
};

stopBtn.onclick = () => {
recognition.stop();
};
