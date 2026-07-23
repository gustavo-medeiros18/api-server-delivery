from datetime import datetime

# Classe datetime representa data
# juntamente com informações sobre
# horário. Por padrão, no formato
# ano-mês-dia horas:minutos:segundos.

# ordem dos parâmetros na chamada:
# ano, mês, dia, horas, minutos,
# segundos.
data_e_hora = datetime(2026, 6, 22, 10, 30, 0)
print(f"Data e hora criada: {data_e_hora}")
print(f"Tipo da data e hora criada: {type(data_e_hora)}")
