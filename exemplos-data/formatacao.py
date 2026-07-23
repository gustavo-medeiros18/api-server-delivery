from datetime import datetime

date_e_hora_atual = datetime.now()
print(f"Data e hora atual: {date_e_hora_atual}")
print(f"Tipo da data e hora atual: {type(date_e_hora_atual)}\n")

# Para formatar uma data (classe datetime), pode
# ser utilizada a função strftime. Que realiza a 
# operação contrária a strptime. A função strftime
# recebe como parâmetro uma string que serve como
# "modelo" do formato que a data ficará como string.
FORMATO_DATA = "%Y-%m-%dT%H:%M:%S"
date_e_hora_atual_formatada = date_e_hora_atual.strftime(FORMATO_DATA)
print(f"Data e hora atual (formatada): {date_e_hora_atual_formatada}")
print(f"Tipo da data e hora atual (formatada): {type(date_e_hora_atual_formatada)}")
