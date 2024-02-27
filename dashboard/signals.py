from django.db.models.signals import post_save
from dashboard.models import Atendimento
from django.dispatch import receiver

@receiver(post_save, sender=Atendimento)
def atualizar_agendamento(sender, instance, created, **kwargs):
    print('Signal chamado com sucesso ')
    
    '''if created:
        agendamento = instance.agendamento
        print(agendamento)
        agendamento.atendido = True
        agendamento.save()
        print('Atendido mudado para True')
    print('else do if created')'''

post_save.connect(atualizar_agendamento, sender=Atendimento)
