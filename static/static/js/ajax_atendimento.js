console.log("O script ajax está funcionando!");

$(document).ready(function() {
    $('#IDatendimento').click(function() {
        $.ajax({
            url: '{% url "dashboard:atendimento_form" %}',
            type: 'GET',
            success: function(data) {
                $('#formularioAtendimento').html(data);
            },
            error: function() {
                console.log('Erro ao carregar o formulário de atendimento.');
            }
        });
    });
});

