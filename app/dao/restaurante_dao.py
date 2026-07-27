from sqlalchemy.orm import Session
from app.models.restaurante_model import RestauranteModel

def criar(sessao_banco: Session, modelo_dados: RestauranteModel):
    sessao_banco.add(modelo_dados)
    sessao_banco.commit()
    sessao_banco.refresh(modelo_dados)

    return modelo_dados

def listar(sessao_banco: Session):
    modelos_dados = sessao_banco.query(RestauranteModel).all()
    return modelos_dados

def buscar_por_id(
    sessao_banco: Session,
    id: int
):
    modelo_dados = (
        sessao_banco
        .query(RestauranteModel)
        .filter(RestauranteModel.id == id)
        .first()
    )

    
    return modelo_dados

def deletar(
    sessao_banco: Session,
    modelo_dados: RestauranteModel
):
    sessao_banco.delete(modelo_dados)
    sessao_banco.commit()