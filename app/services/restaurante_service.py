from sqlalchemy.orm import Session

from app.models.restaurante_model import Restaurante
from app.schemas.restaurante_schema import RestauranteCriacao
from app.dao.restaurante_dao import criar

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

    restaurante_criado = criar(banco, novo_restaurante)
    return restaurante_criado
