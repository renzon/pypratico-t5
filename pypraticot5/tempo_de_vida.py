from datetime import datetime


def calcular_minutos(nascimento):
    datahora_atual = agora()
    time_delta = datahora_atual - nascimento
    segundos = time_delta.total_seconds()
    minutos = int(segundos / 60)
    return minutos

# não mexa nesse código, está aqui para fim de testes
def agora():
    return datetime.now()
