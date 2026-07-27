from sqlalchemy.orm import Session
from app.models.restaurante_model import RestauranteModel

def criar(sessao_banco: Session, modelo_dados: RestauranteModel):
    sessao_banco.add(modelo_dados)
    sessao_banco.commit()
    sessao_banco.refresh(modelo_dados)

    return modelo_dados