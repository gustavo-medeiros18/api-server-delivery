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
    lista_restaurantes = restaurante_dao.listar(sessao_banco)
    return lista_restaurantes