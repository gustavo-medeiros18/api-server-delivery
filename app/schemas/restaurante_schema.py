from pydantic import BaseModel, Field

# classe NomeClasse(ClasseBase):
#     campo_1
#     campo_2
#     campo_3
class RestauranteCriacaoSchema(BaseModel):
    # min_length = quantidade minima de caracteres para o campo
    # max_length = quantidade maxima de caracteres para o campo
    nome: str = Field(
        min_length=3, 
        max_length=100
    )
    rua: str = Field(
        min_length=3, 
        max_length=255
    )
    bairro: str = Field(
        min_length=3, 
        max_length=100
    )
    # gt = greater than (maior que)
    numero: int = Field(
        gt=0
    )
    cidade: str = Field(
        min_length=3, 
        max_length=100
    )
    categoria: str = Field(
        min_length=3, 
        max_length=100
    )
