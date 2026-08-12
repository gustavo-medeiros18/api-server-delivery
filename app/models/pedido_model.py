from datetime import datetime, UTC
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import relationship
from app.banco_de_dados import modelo_base

def obter_data_atual():
    formato = "%Y-%m-%dT%H:%M:%S"

    data_e_hora_atual = datetime.now()
    data_e_hora_atual_formatadas = data_e_hora_atual.strftime(formato)

    return data_e_hora_atual_formatadas

class PedidoModel(modelo_base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    prato_principal = Column(String, nullable=False)
    acompanhamento = Column(String, nullable=False)
    observacao = Column(String)
    valor = Column(Float, nullable=False)

    id_restaurante = Column(
        Integer,
        ForeignKey("restaurantes.id"),
        nullable=False
    )

    criado_em = Column(
        String,
        default=obter_data_atual,
    )

    atualizado_em = Column(
        String,
        default=obter_data_atual,
        onupdate=obter_data_atual,
    )

    restaurante = relationship(
        "RestauranteModel",
        back_populates="pedidos"
    )