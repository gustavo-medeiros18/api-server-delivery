from pydantic import BaseModel

class CarroSchema(BaseModel):
    placa: str
    ano_fabricacao: int
    modelo: str
    dono: str

# Todo schema definido pode ser chamado como se fosse
# uma função, tendo seus atributos preenchidos como
# parâmetros nomeados para obtermos uma variável
# representando dados que vieram no corpo de uma
# requisição.
dados_carro_corpo = CarroSchema(
    placa="cdc-2026",
    ano_fabricacao=2025,
    modelo="Jeep",
    dono="Fulano"
)

print(f"Dados da variável: {dados_carro_corpo}")

# O tipo da variável dados_carro_corpo será CarroSchema,
# que é a classe a qual ela pertence
print(type(dados_carro_corpo))