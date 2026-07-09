from pydantic import BaseModel, Field
from datetime import datetime

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

class RestauranteResposta(BaseModel):
    id: int
    nome: str
    rua: str
    bairro: str
    numero: int
    cidade: str
    categoria: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True