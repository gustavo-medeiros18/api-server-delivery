from pydantic import BaseModel, Field

class PedidoCriacaoSchema(BaseModel):
    prato_principal: str = Field(
        min_length=3,
        max_length=100
    )

    acompanhamento: str = Field(
        min_length=3,
        max_length=100
    )

    observacao: str | None = Field(
        default=None,
        max_length=100
    )

    valor: float = Field(
        gt=0
    )

    id_restaurante: int = Field(
        gt=0
    )

class PedidoRespostaSchema(BaseModel):
    id: int
    prato_principal: str
    acompanhamento: str
    observacao: str | None
    valor: float
    id_restaurante: int
    criado_em: str
    atualizado_em: str

    class Config:
        from_attributes = True