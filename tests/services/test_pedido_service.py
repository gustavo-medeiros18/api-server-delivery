from unittest.mock import Mock

import pytest
from fastapi import HTTPException, status

from app.models.pedido_model import PedidoModel
from app.models.restaurante_model import RestauranteModel
from app.schemas.pedido_schema import PedidoAlteracaoSchema, PedidoCriacaoSchema
from app.services import pedido_service

def test_criar_monta_modelo_e_retorna_resultado_do_dao(monkeypatch):
    sessao_simulada = Mock()
    dados_entrada = PedidoCriacaoSchema(
        prato_principal="Feijoada",
        acompanhamento="Arroz",
        observacao="Sem pimenta",
        valor=35.5,
        id_restaurante=4,
    )
    pedido_criado_simulado = Mock(spec=PedidoModel)

    criar_dao_simulado = Mock(return_value=pedido_criado_simulado)
    monkeypatch.setattr(pedido_service.pedido_dao, "criar", criar_dao_simulado)
    resultado = pedido_service.criar(sessao_simulada, dados_entrada)

    modelo_criado_service = criar_dao_simulado.call_args.args[1]
    assert resultado is pedido_criado_simulado
    assert isinstance(modelo_criado_service, PedidoModel)
    assert modelo_criado_service.prato_principal == dados_entrada.prato_principal
    assert modelo_criado_service.acompanhamento == dados_entrada.acompanhamento
    assert modelo_criado_service.observacao == dados_entrada.observacao
    assert modelo_criado_service.valor == dados_entrada.valor
    assert modelo_criado_service.id_restaurante == dados_entrada.id_restaurante
    criar_dao_simulado.assert_called_once_with(sessao_simulada, modelo_criado_service)

def test_listar_retorna_lista_do_dao(monkeypatch):
    sessao = Mock()
    pedidos = [Mock(spec=PedidoModel)]

    listar_dao = Mock(return_value=pedidos)
    monkeypatch.setattr(pedido_service.pedido_dao, "listar", listar_dao)
    resultado = pedido_service.listar(sessao)

    assert resultado is pedidos
    listar_dao.assert_called_once_with(sessao)

def test_alterar_retorna_none_quando_pedido_nao_existe(monkeypatch):
    sessao = Mock()

    buscar_dao = Mock(return_value=None)
    alterar_dao = Mock()
    monkeypatch.setattr(pedido_service.pedido_dao, "buscar_pedido", buscar_dao)
    monkeypatch.setattr(pedido_service.pedido_dao, "alterar", alterar_dao)
    resultado = pedido_service.alterar(
        sessao,
        7,
        PedidoAlteracaoSchema(prato_principal="Pizza"),
    )

    assert resultado is None
    buscar_dao.assert_called_once_with(sessao, 7)
    alterar_dao.assert_not_called()

def test_alterar_atualiza_pedido_sem_validar_novo_restaurante(monkeypatch):
    sessao = Mock()
    pedido = Mock(spec=PedidoModel)
    pedido_atualizado = Mock(spec=PedidoModel)
    dados = PedidoAlteracaoSchema(prato_principal="Pizza", valor=42)

    monkeypatch.setattr(
        pedido_service.pedido_dao,
        "buscar_pedido",
        Mock(return_value=pedido),
    )
    alterar_dao = Mock(return_value=pedido_atualizado)
    buscar_restaurante_dao = Mock()
    monkeypatch.setattr(pedido_service.pedido_dao, "alterar", alterar_dao)
    monkeypatch.setattr(
        pedido_service.restaurante_dao,
        "buscar_restaurante",
        buscar_restaurante_dao,
    )
    resultado = pedido_service.alterar(sessao, 7, dados)

    assert resultado is pedido_atualizado
    buscar_restaurante_dao.assert_not_called()
    alterar_dao.assert_called_once_with(
        sessao,
        pedido,
        {"prato_principal": "Pizza", "valor": 42},
    )

def test_alterar_valida_restaurante_e_atualiza_pedido(monkeypatch):
    sessao = Mock()
    pedido = Mock(spec=PedidoModel)
    restaurante = Mock(spec=RestauranteModel)
    pedido_atualizado = Mock(spec=PedidoModel)
    dados = PedidoAlteracaoSchema(id_restaurante=9)

    monkeypatch.setattr(
        pedido_service.pedido_dao,
        "buscar_pedido",
        Mock(return_value=pedido),
    )
    buscar_restaurante_dao = Mock(return_value=restaurante)
    alterar_dao = Mock(return_value=pedido_atualizado)
    monkeypatch.setattr(
        pedido_service.restaurante_dao,
        "buscar_restaurante",
        buscar_restaurante_dao,
    )
    monkeypatch.setattr(pedido_service.pedido_dao, "alterar", alterar_dao)
    resultado = pedido_service.alterar(sessao, 7, dados)

    assert resultado is pedido_atualizado
    buscar_restaurante_dao.assert_called_once_with(sessao, 9)
    alterar_dao.assert_called_once_with(sessao, pedido, {"id_restaurante": 9})

def test_alterar_rejeita_restaurante_inexistente(monkeypatch):
    sessao = Mock()
    pedido = Mock(spec=PedidoModel)

    monkeypatch.setattr(
        pedido_service.pedido_dao,
        "buscar_pedido",
        Mock(return_value=pedido),
    )
    monkeypatch.setattr(
        pedido_service.restaurante_dao,
        "buscar_restaurante",
        Mock(return_value=None),
    )
    alterar_dao = Mock()
    monkeypatch.setattr(pedido_service.pedido_dao, "alterar", alterar_dao)
    with pytest.raises(HTTPException) as excecao:
        pedido_service.alterar(
            sessao,
            7,
            PedidoAlteracaoSchema(id_restaurante=9),
        )

    assert excecao.value.status_code == status.HTTP_404_NOT_FOUND
    assert excecao.value.detail == "Restaurante não encontrado"
    alterar_dao.assert_not_called()

def test_excluir_retorna_none_quando_pedido_nao_existe(monkeypatch):
    sessao = Mock()

    buscar_dao = Mock(return_value=None)
    excluir_dao = Mock()
    monkeypatch.setattr(pedido_service.pedido_dao, "buscar_pedido", buscar_dao)
    monkeypatch.setattr(pedido_service.pedido_dao, "excluir", excluir_dao)
    resultado = pedido_service.excluir(sessao, 7)

    assert resultado is None
    buscar_dao.assert_called_once_with(sessao, 7)
    excluir_dao.assert_not_called()

def test_excluir_remove_pedido_existente(monkeypatch):
    sessao = Mock()
    pedido = Mock(spec=PedidoModel)

    buscar_dao = Mock(return_value=pedido)
    excluir_dao = Mock()
    monkeypatch.setattr(pedido_service.pedido_dao, "buscar_pedido", buscar_dao)
    monkeypatch.setattr(pedido_service.pedido_dao, "excluir", excluir_dao)
    resultado = pedido_service.excluir(sessao, 7)

    assert resultado is pedido
    buscar_dao.assert_called_once_with(sessao, 7)
    excluir_dao.assert_called_once_with(sessao, pedido)
