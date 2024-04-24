document.addEventListener('DOMContentLoaded', function() {
    const inputData = document.querySelector('#id_data_consulta');

    inputData.addEventListener('input', function() {
        let data = inputData.value.replace(/\D/g, '');

        if (data.length > 0) {
            if (data.length > 2) {
                data = data.substring(0, 2) + '/' + data.substring(2);
            }
            if (data.length > 5) {
                data = data.substring(0, 5) + '/' + data.substring(5, 9);
            }
        }
        inputData.value = data;
    });
});

