from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.restaurante_model import Restaurante
from app.schemas.restaurante_schema import RestauranteAlteracao, RestauranteCriacao
from app.dao.restaurante_dao import buscar_por_id, atualizar, criar, listar, deletar

def criar_restaurante(
    banco: Session,
    restaurante: RestauranteCriacao
):
    novo_restaurante = Restaurante(
        nome=restaurante.nome,
        rua=restaurante.rua,
        bairro=restaurante.bairro,
        numero=restaurante.numero,
        cidade=restaurante.cidade,
        categoria=restaurante.categoria
    )

    resturante_criado = criar(banco, novo_restaurante)
    return resturante_criado
