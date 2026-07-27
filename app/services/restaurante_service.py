from sqlalchemy.orm import Session
from app.schemas.restaurante_schema import RestauranteCriacaoSchema
from app.models.restaurante_model import RestauranteModel
from app.dao import restaurante_dao

def criar(sessao_banco: Session, dados_restaurante: RestauranteCriacaoSchema):
    modelo_dados = RestauranteModel(
        nome=dados_restaurante.nome,
        rua=dados_restaurante.rua,
        bairro=dados_restaurante.bairro,
        numero = dados_restaurante.numero,
        cidade=dados_restaurante.cidade,
        categoria=dados_restaurante.categoria
    )

    restaurante_criado = restaurante_dao.criar(sessao_banco, modelo_dados)
    return restaurante_criado

def listar(sessao_banco: Session):
    restaurantes_cadastrados = restaurante_dao.listar(sessao_banco)
    return restaurantes_cadastrados

def deletar(
    sessao_banco: Session,
    id: int
):
    restaurante_encontrado = restaurante_dao.buscar_por_id(
        sessao_banco,
        id
    )

    if restaurante_encontrado is None:
        return None

    restaurante_dao.deletar(sessao_banco, restaurante_encontrado)

    return restaurante_encontrado