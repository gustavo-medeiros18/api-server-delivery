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

def buscar_restaurante(sessao_banco: Session, id_restaurante_encontrar: int):
    consulta = sessao_banco.query(RestauranteModel)
    consulta_com_filtro = consulta.filter(RestauranteModel.id == id_restaurante_encontrar)

    # modelo_dados armazena o restaurante
    # que foi encontrado ou nada (None)
    modelo_dados = consulta_com_filtro.one_or_none()
    return modelo_dados

def atualizar(
    sessao_banco: Session,
    modelo_dados: RestauranteModel,
    dados_atualizacao: dict
):
    for campo, valor in dados_atualizacao.items():
        setattr(modelo_dados, campo, valor)

    sessao_banco.commit()
    sessao_banco.refresh(modelo_dados)

    return modelo_dados

def excluir(sessao_banco: Session, modelo_dados: RestauranteModel):
    # modelo_dados representa o restaurante
    # que se deseja excluir.
    sessao_banco.delete(modelo_dados)
    sessao_banco.commit()