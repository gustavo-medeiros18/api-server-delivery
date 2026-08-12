from pydantic import BaseModel, Field

class PedidoCriacaoSchema(BaseModel):
    prato_principal: str = Field(
        min_length=3,
        max_length=255
    )
    acompanhamento: str = Field(
        min_length=3,
        max_length=255
    )
    observacao: str | None = Field(
        default=None,
        max_length=500
    )
    valor: float = Field(gt=0)
    id_restaurante: int

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
