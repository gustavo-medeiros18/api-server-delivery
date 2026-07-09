from sqlalchemy.orm import Session

from app.models.restaurante_model import Restaurante
from app.schemas.restaurante_schema import RestauranteCriacaoSchema
from app.dao import restaurante_dao

def criar(
    banco: Session,
    restaurante: RestauranteCriacaoSchema
):
    novo_restaurante = Restaurante(
        nome=restaurante.nome,
        rua=restaurante.rua,
        bairro=restaurante.bairro,
        numero=restaurante.numero,
        cidade=restaurante.cidade,
        categoria=restaurante.categoria
    )

    restaurante_criado = restaurante_dao.criar(banco, novo_restaurante)
    return restaurante_criado
