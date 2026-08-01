from pydantic import BaseModel

class CarroSchema(BaseModel):
    placa: str
    ano_fabricacao: int
    modelo: str
    dono: str | None

# Todo schema definido pode ser chamado como se fosse
# uma função, tendo seus atributos preenchidos como
# parâmetros nomeados para obtermos uma variável
# representando dados que vieram no corpo de uma
# requisição.
dados_carro_corpo = CarroSchema(
    placa="cdc-2026",
    ano_fabricacao=2025,
    modelo="Jeep",
    dono=None
)

# O tipo da variável dados_carro_corpo será CarroSchema,
# que é a classe a qual ela pertence
print(type(dados_carro_corpo))

# model_dump é uma função (específica de variáveis
# que são schemas) que retorna um dicionário com os
# dados presentes nessa variável.
dicionario_dados = dados_carro_corpo.model_dump(exclude_unset=True)

# O tipo da variável dicionario_dados é dict
print(type(dicionario_dados))
