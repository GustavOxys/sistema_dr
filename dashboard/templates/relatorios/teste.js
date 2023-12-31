function updateTimer() {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;

    // Formate os valores com dois dígitos, adicionando zeros à esquerda, se necessário
    const formattedTime = `${padZero(hours)}:${padZero(minutes)}:${padZero(remainingSeconds)}`;

    document.getElementById('timer').textContent = `Duração: ${formattedTime}`;
}

function padZero(value) {
    return value < 10 ? `0${value}` : value;
}

document.addEventListener('DOMContentLoaded', function() {
    let timer;
    let seconds = 0;

    document.getElementById('startButton').addEventListener('click', function() {
        if (!timer) {
            timer = setInterval(function() {
                seconds++;
                updateTimer();
            }, 1000); // 1000ms = 1 segundo
        }
    });
});