from sqlalchemy.orm import Session
from app.models.restaurante_model import RestauranteModel

def criar(sessao_banco: Session, modelo_dados: RestauranteModel):
    sessao_banco.add(modelo_dados)
    sessao_banco.commit()
    sessao_banco.refresh(modelo_dados)

    return modelo_dados

def listar(sessao_banco: Session):
    consulta = sessao_banco.query(RestauranteModel)

    # modelo_dados armazena uma lista
    # com todos os restaurantes dentro
    # da tabela.
    modelo_dados = consulta.all()
    return modelo_dados