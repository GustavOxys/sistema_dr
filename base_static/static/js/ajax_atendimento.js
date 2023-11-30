$(document).ready(function() {
    $('#IDatendimento').click(function(event) {
        event.preventDefault();  // Impede o link de executar a ação padrão (navegar para outra página)

        console.log("Função Ajax foi chamada.");
        var pacienteId = '12';
        console.log("Paciente ID:", pacienteId);


        // Faz a solicitação Ajax para a URL desejada
        $.ajax({
            url: '/atendimento/' + pacienteId + '/',
            type: 'GET',
            dataType: 'html',
            success: function(response) {
                $('#form-atendimento').replaceWith(response);
            }
        });
        
        console.log('depois da func ajax')
    });
});
