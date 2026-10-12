from unittest.mock import Mock
from app.models.pedido_model import PedidoModel
from app.services import pedido_service
from app.schemas.pedido_schema import PedidoCriacaoSchema

def test_criar(monkeypatch):
    sessao_simulada = Mock()

    retorno_dao_simulado = Mock(spec=PedidoModel)
    criar_dao_simulado = Mock(return_value=retorno_dao_simulado)

    monkeypatch.setattr(
        pedido_service.pedido_dao,
        "criar",
        criar_dao_simulado
    )

    dados_entrada_exemplo = PedidoCriacaoSchema(
        prato_principal="Feijoada",
        acompanhamento="Arroz",
        observacao="Sem pimenta",
        valor=35.0,
        id_restaurante=4
    )

    resultado = pedido_service.criar(
        sessao_simulada,
        dados_entrada_exemplo
    )

    