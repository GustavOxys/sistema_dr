document.addEventListener('DOMContentLoaded', function() {
    const inputCpf = document.querySelector('#id_cpf');

    inputCpf.addEventListener('input', function() {
        let valor = inputCpf.value.replace(/\D/g, '');

        if (valor.length > 0) {
            valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
            valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
            valor = valor.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        }

        inputCpf.value = valor;
    });
});
