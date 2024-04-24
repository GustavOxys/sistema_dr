// Seleciona o ícone do usuário e a caixa de informações do usuário
var userIcon = document.querySelector('.user-icon');
var userInfoBox = document.querySelector('.user-info-box');

// Adiciona um evento de clique ao ícone do usuário
userIcon.addEventListener('click', function() {
    // Verifica se a caixa de informações está visível
    if (userInfoBox.style.display === 'none') {
        // Se estiver oculta, exibe a caixa de informações
        userInfoBox.style.display = 'flex';
    } else {
        // Caso contrário, oculta a caixa de informações
        userInfoBox.style.display = 'none';
    }
});

// Adiciona um ouvinte de evento para o clique fora da caixa de informações
document.addEventListener('click', function(event) {
    // Verifica se o clique foi fora da caixa de informações e fora do ícone do usuário
    if (!userIcon.contains(event.target) && !userInfoBox.contains(event.target)) {
        // Se foi fora da caixa de informações e fora do ícone do usuário, oculta a caixa de informações
        userInfoBox.style.display = 'none';
    }
});