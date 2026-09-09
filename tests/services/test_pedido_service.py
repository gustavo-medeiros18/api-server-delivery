from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException, status

from app.models.pedido_model import PedidoModel
from app.models.restaurante_model import RestauranteModel
from app.schemas.pedido_schema import PedidoAlteracaoSchema, PedidoCriacaoSchema
from app.services import pedido_service


class TestPedidoService:
    def test_criar_monta_modelo_e_retorna_resultado_do_dao(self):
        sessao = Mock()
        dados = PedidoCriacaoSchema(
            prato_principal="Feijoada",
            acompanhamento="Arroz",
            observacao="Sem pimenta",
            valor=35.5,
            id_restaurante=4,
        )
        pedido_criado = Mock(spec=PedidoModel)

        with patch.object(
            pedido_service.pedido_dao,
            "criar",
            return_value=pedido_criado,
        ) as criar_dao:
            resultado = pedido_service.criar(sessao, dados)

        modelo = criar_dao.call_args.args[1]
        assert resultado is pedido_criado
        assert isinstance(modelo, PedidoModel)
        assert modelo.prato_principal == dados.prato_principal
        assert modelo.acompanhamento == dados.acompanhamento
        assert modelo.observacao == dados.observacao
        assert modelo.valor == dados.valor
        assert modelo.id_restaurante == dados.id_restaurante
        criar_dao.assert_called_once_with(sessao, modelo)

    def test_listar_retorna_lista_do_dao(self):
        sessao = Mock()
        pedidos = [Mock(spec=PedidoModel)]

        with patch.object(
            pedido_service.pedido_dao,
            "listar",
            return_value=pedidos,
        ) as listar_dao:
            resultado = pedido_service.listar(sessao)

        assert resultado is pedidos
        listar_dao.assert_called_once_with(sessao)

    def test_alterar_retorna_none_quando_pedido_nao_existe(self):
        sessao = Mock()

        with patch.object(
            pedido_service.pedido_dao,
            "buscar_pedido",
            return_value=None,
        ) as buscar_dao, patch.object(
            pedido_service.pedido_dao,
            "alterar",
        ) as alterar_dao:
            resultado = pedido_service.alterar(
                sessao,
                7,
                PedidoAlteracaoSchema(prato_principal="Pizza"),
            )

        assert resultado is None
        buscar_dao.assert_called_once_with(sessao, 7)
        alterar_dao.assert_not_called()

    def test_alterar_atualiza_pedido_sem_validar_novo_restaurante(self):
        sessao = Mock()
        pedido = Mock(spec=PedidoModel)
        pedido_atualizado = Mock(spec=PedidoModel)
        dados = PedidoAlteracaoSchema(prato_principal="Pizza", valor=42)

        with patch.object(
            pedido_service.pedido_dao,
            "buscar_pedido",
            return_value=pedido,
        ), patch.object(
            pedido_service.pedido_dao,
            "alterar",
            return_value=pedido_atualizado,
        ) as alterar_dao, patch.object(
            pedido_service.restaurante_dao,
            "buscar_restaurante",
        ) as buscar_restaurante_dao:
            resultado = pedido_service.alterar(sessao, 7, dados)

        assert resultado is pedido_atualizado
        buscar_restaurante_dao.assert_not_called()
        alterar_dao.assert_called_once_with(
            sessao,
            pedido,
            {"prato_principal": "Pizza", "valor": 42},
        )

    def test_alterar_valida_restaurante_e_atualiza_pedido(self):
        sessao = Mock()
        pedido = Mock(spec=PedidoModel)
        restaurante = Mock(spec=RestauranteModel)
        pedido_atualizado = Mock(spec=PedidoModel)
        dados = PedidoAlteracaoSchema(id_restaurante=9)

        with patch.object(
            pedido_service.pedido_dao,
            "buscar_pedido",
            return_value=pedido,
        ), patch.object(
            pedido_service.restaurante_dao,
            "buscar_restaurante",
            return_value=restaurante,
        ) as buscar_restaurante_dao, patch.object(
            pedido_service.pedido_dao,
            "alterar",
            return_value=pedido_atualizado,
        ) as alterar_dao:
            resultado = pedido_service.alterar(sessao, 7, dados)

        assert resultado is pedido_atualizado
        buscar_restaurante_dao.assert_called_once_with(sessao, 9)
        alterar_dao.assert_called_once_with(sessao, pedido, {"id_restaurante": 9})

    def test_alterar_rejeita_restaurante_inexistente(self):
        sessao = Mock()
        pedido = Mock(spec=PedidoModel)

        with patch.object(
            pedido_service.pedido_dao,
            "buscar_pedido",
            return_value=pedido,
        ), patch.object(
            pedido_service.restaurante_dao,
            "buscar_restaurante",
            return_value=None,
        ), patch.object(
            pedido_service.pedido_dao,
            "alterar",
        ) as alterar_dao:
            with pytest.raises(HTTPException) as excecao:
                pedido_service.alterar(
                    sessao,
                    7,
                    PedidoAlteracaoSchema(id_restaurante=9),
                )

        assert excecao.value.status_code == status.HTTP_404_NOT_FOUND
        assert excecao.value.detail == "Restaurante não encontrado"
        alterar_dao.assert_not_called()

    def test_excluir_retorna_none_quando_pedido_nao_existe(self):
        sessao = Mock()

        with patch.object(
            pedido_service.pedido_dao,
            "buscar_pedido",
            return_value=None,
        ) as buscar_dao, patch.object(
            pedido_service.pedido_dao,
            "excluir",
        ) as excluir_dao:
            resultado = pedido_service.excluir(sessao, 7)

        assert resultado is None
        buscar_dao.assert_called_once_with(sessao, 7)
        excluir_dao.assert_not_called()

    def test_excluir_remove_pedido_existente(self):
        sessao = Mock()
        pedido = Mock(spec=PedidoModel)

        with patch.object(
            pedido_service.pedido_dao,
            "buscar_pedido",
            return_value=pedido,
        ) as buscar_dao, patch.object(
            pedido_service.pedido_dao,
            "excluir",
        ) as excluir_dao:
            resultado = pedido_service.excluir(sessao, 7)

        assert resultado is pedido
        buscar_dao.assert_called_once_with(sessao, 7)
        excluir_dao.assert_called_once_with(sessao, pedido)
