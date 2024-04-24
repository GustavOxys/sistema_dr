document.addEventListener('DOMContentLoaded', function() {
    const inputTime = document.querySelector('#id_hora_consulta');

    inputTime.addEventListener('input', function() {
        let valor = inputTime.value;

        // Remover qualquer caractere que não seja um dígito
        valor = valor.replace(/\D/g, '');

        // Adicionar ':' após os dois primeiros números, se ainda não houver
        if (valor.length > 2 && valor.indexOf(':') === -1) {
            valor = valor.substring(0, 2) + ':' + valor.substring(2);
        }

        // Definir o valor atualizado no campo de entrada
        inputTime.value = valor;
    });
});
