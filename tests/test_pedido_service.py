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

    modelo_dados_construido = criar_dao_simulado.call_args.args[1]
    assert resultado is retorno_dao_simulado
    assert isinstance(modelo_dados_construido, PedidoModel)
    assert modelo_dados_construido.prato_principal == dados_entrada_exemplo.prato_principal
    assert modelo_dados_construido.acompanhamento == dados_entrada_exemplo.acompanhamento
    assert modelo_dados_construido.observacao == dados_entrada_exemplo.observacao
    assert modelo_dados_construido.valor == dados_entrada_exemplo.valor
    assert modelo_dados_construido.id_restaurante == dados_entrada_exemplo.id_restaurante
    
    criar_dao_simulado.assert_called_with(sessao_simulada, modelo_dados_construido)

def test_listar(monkeypatch):
    sessao_simulada = Mock()

    pedido_simulado = Mock(spec=PedidoModel)
    retorno_dao_simulado = [pedido_simulado]

    listar_dao_simulado = Mock(return_value=retorno_dao_simulado)
    monkeypatch.setattr(
        pedido_service.pedido_dao,
        "listar",
        listar_dao_simulado
    )

    resultado = pedido_service.listar(sessao_simulada)

    assert resultado is retorno_dao_simulado
    listar_dao_simulado.assert_called_with(sessao_simulada)