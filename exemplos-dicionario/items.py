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
items = dicionario_dados.items()
print(items)
