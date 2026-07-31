from sqlalchemy.orm import Session
from app.schemas.restaurante_schema import RestauranteCriacaoSchema, RestauranteAlteracaoSchema
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

def atualizar(
    sessao_banco: Session,
    id_restaurante_atualizar: int,
    dados_atualizacao_restaurante: RestauranteAlteracaoSchema
):
    restaurante_existente = restaurante_dao.buscar_restaurante(
        sessao_banco,
        id_restaurante_atualizar
    )

    if not restaurante_existente:
        return None

    dados_atualizacao = dados_atualizacao_restaurante.model_dump(
        exclude_unset=True
    )

    restaurante_atualizado = restaurante_dao.atualizar(sessao_banco, restaurante_existente, dados_atualizacao)
    return restaurante_atualizado

def excluir(sessao_banco: Session, id_restaurante_excluir: int):
    restaurante_encontrado = restaurante_dao.buscar_restaurante(sessao_banco, id_restaurante_excluir)

    if restaurante_encontrado == None:
        return None

    restaurante_dao.excluir(sessao_banco, restaurante_encontrado)

    return restaurante_encontrado