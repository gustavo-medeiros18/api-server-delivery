from sqlalchemy.orm import Session

from app.models.restaurante_model import Restaurante

def criar(
    banco: Session,
    novo_restaurante: Restaurante
):
    banco.add(novo_restaurante)
    banco.commit()
    banco.refresh(novo_restaurante)

    return novo_restaurante
