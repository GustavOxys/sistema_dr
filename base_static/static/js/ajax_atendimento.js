$(document).ready(function() {
    $('#IDatendimento').click(function() {
        console.log("Função ajax foi chamada.");
        $.ajax({
            url: '{% url "dashboard:atendimento_form" paciente_id=paciente.id %}',
            type: 'POST',
            success: function(response) {
                // Exibe o formulário de atendimento
                $('#form-atendimento').html(response.form);
            }
        });
    });
});