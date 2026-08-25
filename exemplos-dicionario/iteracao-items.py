dicionario_dados = {
    "placa": "cdc-2026",
    "ano_fabricacao": 2025,
    "modelo": "Jeep",
    "dono": "Fulano"
}

# A função items, que é uma função específica de dicionários
# permite obter uma estrutura semelhante a uma lista de tuplas,
# em que cada elemento é um dos pares chave-valor que compõem
# um dicionário.
itens_dicionario = dicionario_dados.items()
print(itens_dicionario, "\n")

# É possível iterar sobre os pares campo-valor existentes
# dentro de um dicionário, através da iteração sobre uma
# variável que armazene o retorno da função items().

# Necessário usar a sintaxe geral:
# for campo, valor in <nome_da_variavel_items>
for campo, valor in itens_dicionario:
    print(f"iterando sobre o campo {campo}, que possui o valor {valor}")