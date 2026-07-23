from datetime import datetime

# Classe datetime representa data
# juntamente com informações sobre
# horário. Por padrão, no formato
# ano-mês-dia hora:minuto:segundo.

# ordem dos parâmetros na chamada:
# ano, mês, dia, hora, minuto,
# segundo.
data_e_hora = datetime(2026, 6, 22, 10, 30, 0)
print(f"Data e hora criada: {data_e_hora}")

# Para obter uma data que represente
# o dia e horário atual, sem necessidade
# de passar parâmetros, pode ser
# utilizado a função now() dessa classe
# datetime:
date_e_hora_atual = datetime.now()
print(f"Data e hora atual: {date_e_hora_atual}")