from datetime import datetime


def calcular_minutos(nascimento):
    datahora_atual = datetime.now()
    time_delta = datahora_atual - nascimento
    segundos = time_delta.total_seconds()
    minutos = int(segundos / 60)
    return minutos
