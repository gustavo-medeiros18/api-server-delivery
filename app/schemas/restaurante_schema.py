from pydantic import BaseModel, Field

# classe NomeClasse(ClasseBase):
#     campo_1
#     campo_2
#     campo_3
class RestauranteCriacaoSchema(BaseModel):
    nome: str
    rua: str
    bairro: str
    numero: int
    cidade: str
    categoria: str
