from pydantic import BaseModel

class CarroSchema(BaseModel):
    placa: str
    ano_fabricacao: int
    modelo: str
    dono: str

dados_carro_corpo = CarroSchema(
    placa="cdc-2026",
    ano_fabricacao=2025,
    modelo="Jeep",
    dono="Fulano"
)

dicionario_dados = {
    "placa": "pip-2000",
    "ano_fabricacao": 2026,
}
itens_dicionario = dicionario_dados.items()

print(f"Dados da variável de schema antes da alteração: {dados_carro_corpo}\n")

for campo, valor in itens_dicionario:
    print(f"Atribuindo o valor contido no campo {campo} para {valor}")

    # A função setattr() pode ser utilizada dentro de uma iteração
    # para percorrer um dicionário e atribuir os valores de cada
    # campo a cada atributo correspondente dentro de uma classe,
    # que pode ser tanto uma classe de schema como uma classe de
    # modelo de dados.

    # Muito utilizada na prática para alterar os valores de determinados
    # atributos de um schema ou modelo de dados com o conteúdo de um
    # dicionário.
    setattr(dados_carro_corpo, campo, valor)

print(f"\nDados da variável de schema após a alteração: {dados_carro_corpo}")