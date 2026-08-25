dicionario_dados = {
    "placa": "cdc-2026",
    "ano_fabricacao": 2025,
    "modelo": "Jeep",
    "dono": "Fulano"
}

# A função items, que é uma função específica de dicionários
# permite obter uma estrutura semelhante a uma lista de tuplas,
# em que cada elemento é um dos pares campo-valor que compõem
# um dicionário.
itens_dicionario = dicionario_dados.items()
print(itens_dicionario)
