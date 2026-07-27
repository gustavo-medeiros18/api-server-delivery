from datetime import datetime

data_e_hora_atual = datetime.now()
print(f"Data e hora atual: {data_e_hora_atual}")
print(f"Tipo da data e hora atual: {type(data_e_hora_atual)}\n")

# Para formatar uma data (classe datetime), pode
# ser utilizada a função strftime. Que realiza a 
# operação contrária a strptime. A função strftime
# recebe como parâmetro uma string que serve como
# "template" do formato que a data ficará como string.
formato = "%Y-%m-%dT%H:%M:%S"
data_e_hora_atual_formatada = data_e_hora_atual.strftime(formato)

print(f"Data e hora atual (formatada): {data_e_hora_atual_formatada}")
print(f"Tipo da data e hora atual (formatada): {type(data_e_hora_atual_formatada)}")
