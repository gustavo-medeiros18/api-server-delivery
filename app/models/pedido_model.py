from app.banco_de_dados import modelo_base
from sqlalchemy import Column, String, Float, Integer
from datetime import datetime

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
    observacao = Column(String, nullable=True)
    valor = Column(Float, nullable=False)

    criado_em = Column(String, default=obter_data_atual)
    atualizado_em = Column(String, default=obter_data_atual, onupdate=obter_data_atual)