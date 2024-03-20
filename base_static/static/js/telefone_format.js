document.addEventListener('DOMContentLoaded', function() {
    const inputTelefone = document.querySelector('#id_telefone');

    inputTelefone.addEventListener('input', function() {
        let valor = inputTelefone.value.replace(/\D/g, '');

        if (valor.length > 0) {
            valor = '(' + valor.substring(0, 2) + ')' + valor.substring(2);
            if (valor.length > 5) {
                valor = valor.substring(0, 5) + ' ' + valor.substring(5);
            }
            if (valor.length > 10) {
                valor = valor.substring(0, 10) + '-' + valor.substring(10);
            }
            if (valor.length > 15) {
                valor = valor.substring(0, 15);
            }
        }
        inputTelefone.value = valor;
    });
});
