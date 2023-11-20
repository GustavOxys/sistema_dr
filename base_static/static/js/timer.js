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
    const sidebarItems = document.getElementById('sidebarItems');
    

    startButton.addEventListener('click', function() {
        if (!timer) {
            timer = setInterval(function() {
                seconds++;
                updateTimer();
            }, 1000); // 1000ms = 1 segundo

            isPressed = true;
            startButton.classList.add('button-pressed'); // Adiciona classe p/ o botão Pressionado           
            startButton.textContent = 'Finalizar Atendimento'; // Altera o texto do botão

            // Adiciona uma classe para mostrar os itens da lista quando clicado o botão
            sidebarItems.classList.add('show-items');
        }
        

        else {
            clearInterval(timer);
            timer = null;
            isPressed = false;
            startButton.classList.remove('button-pressed'); // Remove a classe do botão Pressionado           
            startButton.textContent = 'Iniciar Atendimento'; // Restaura o texto original do botão

            // remove a classe para esconder os itens da lista quando clicado
            sidebarItems.classList.remove('show-items');
        }
    });
});

