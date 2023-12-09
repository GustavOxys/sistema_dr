$(document).ready(function() {
    $('#IDatendimento').click(function(event) {
        event.preventDefault();  // Impede o link de executar a ação padrão (navegar para outra página)
        const currentTime = new Date().getTime();
        console.log(`${currentTime}: LOG js funcao ajax chamada`);
        
        var pacienteId = '12';        
        console.log(`${currentTime}: "Paciente ID:"'`, pacienteId);


        // Faz a solicitação Ajax para a URL desejada
        $.ajax({
            url: '/atendimento/' + pacienteId + '/',
            type: 'GET',
            dataType: 'html',
            
            success: function(response) {
                
                console.log(`${currentTime}: LOG js resposta aquisicao ajax`, response);
                $('#form-atendimento').html(response);            
            },
            error: function() {
                console.log('houve algum erro')
            }
        });       
    });   
});

