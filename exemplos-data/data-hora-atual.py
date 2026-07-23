from datetime import datetime

# Com a classe datetime, para obter uma
# data que represente o dia e horário atual,
# sem necessidade de passar parâmetros, pode
# ser utilizada a função now() dessa classe
# datetime:
data_e_hora_atual = datetime.now()
print(f"Data e hora atual: {data_e_hora_atual}")
print(f"Tipo da data e hora atual: {type(data_e_hora_atual)}")