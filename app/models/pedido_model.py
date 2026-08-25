from app.banco_de_dados import modelo_base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
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

    # O atributo de chave_estrangeira representa a coluna
    # dentro da tabela que será referenciada. Como cada
    # pedido precisará possuir o id do restaurante ao qual
    # está associado, e esse id do restaurante é uma
    # informação que vem de uma tabela externa (isto é, da
    # coluna id dentro da tabela restaurantes), deve ser
    # informada restaurantes.id como parâmetro a classe
    # ForeignKey
    chave_estrangeira = ForeignKey("restaurantes.id")
    id_restaurante = Column(Integer, chave_estrangeira, nullable=False)

    criado_em = Column(String, default=obter_data_atual)
    atualizado_em = Column(String, default=obter_data_atual, onupdate=obter_data_atual)