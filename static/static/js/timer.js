let seconds = 0;

console.log("O script está funcionando!");

function updateTimer() {
    console.log("Função updateTimer foi chamada.");
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
    let isPressed = false; // Adiciona uma variável para rastrear se o botão está pressionado

    const startButton = document.getElementById('startButton');
    const iconElement = startButton.querySelector('i');

    startButton.addEventListener('click', function() {
        if (!timer) {
            timer = setInterval(function() {
                seconds++;
                updateTimer();
            }, 1000); // 1000ms = 1 segundo

            isPressed = true;
            startButton.classList.add('button-pressed'); // Adiciona a classe para o botão pressionado
            iconElement.classList.remove('bi-play-fill'); // Remova a classe do ícone de reprodução
            iconElement.classList.add('bi-stop-fill'); // Adicione a classe do ícone de pausa
            startButton.textContent = 'Finalizar Atendimento'; // Altera o texto do botão
        } else {
            clearInterval(timer);
            timer = null;
            isPressed = false;
            startButton.classList.remove('button-pressed'); // Remove a classe do botão pressionado
            iconElement.classList.remove('bi-stop-fill');
            iconElement.classList.add('bi-play-fill');
            startButton.textContent = 'Iniciar Atendimento'; // Restaura o texto original do botão
        }
    });
});

