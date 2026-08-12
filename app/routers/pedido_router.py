from fastapi import APIRouter, HTTPException,status

from app.banco_de_dados import obter_sessao
from app.schemas.pedido_schema import PedidoCriacaoSchema, PedidoRespostaSchema
from app.services import pedido_service
from app.services import restaurante_service

router = APIRouter()

@router.post(
    "/pedidos",
    response_model=PedidoRespostaSchema,
    status_code=status.HTTP_201_CREATED
)
def criar(
    pedido: PedidoCriacaoSchema
):
    banco = obter_sessao()

    try:
        restaurante_encontrado = restaurante_service.buscar_restaurante(
            banco,
            pedido.id_restaurante
        )

        if restaurante_encontrado == None:
            raise HTTPException(
                status_code=404,
                detail="Restaurante não encontrado"
            )

        pedido_criado = pedido_service.criar(banco, pedido)
        return pedido_criado
    finally:
        banco.close()
