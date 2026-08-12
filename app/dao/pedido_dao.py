from sqlalchemy.orm import Session

from app.models.pedido_model import PedidoModel

def criar(sessao_banco: Session, modelo_dados: PedidoModel):
    sessao_banco.add(modelo_dados)
    sessao_banco.commit()
    sessao_banco.refresh(modelo_dados)

    return modelo_dados