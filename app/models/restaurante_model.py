from banco_de_dados import modelo_base
from sqlalchemy import Column, String, Integer

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