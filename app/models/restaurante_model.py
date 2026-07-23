from banco_de_dados import modelo_base
from sqlalchemy import Column, String, Integer
from datetime import datetime

def obter_data_atual():
    formato = "%Y-%m-%dT%H:%M:%S"

    data_e_hora_atual = datetime.now()
    data_e_hora_atual_formatadas = data_e_hora_atual.strftime(formato)

    return data_e_hora_atual_formatadas

class RestauranteModel(modelo_base):
    __tablename__ = "restaurantes"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)
    rua = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    cidade = Column(String, nullable=False)
    categoria = Column(String, nullable=False)

    criado_em = Column(String)