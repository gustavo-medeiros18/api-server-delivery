from unittest.mock import Mock

import pytest
from fastapi import HTTPException, status

from app.models.pedido_model import PedidoModel
from app.models.restaurante_model import RestauranteModel
from app.schemas.restaurante_schema import (
    RestauranteAlteracaoSchema,
    RestauranteCriacaoSchema,
)
from app.services import restaurante_service


class TestRestauranteService:
    def test_criar_monta_modelo_e_retorna_resultado_do_dao(self, monkeypatch):
        sessao = Mock()
        dados = RestauranteCriacaoSchema(
            nome="Restaurante Central",
            rua="Rua Principal",
            bairro="Centro",
            numero=123,
            cidade="Sao Paulo",
            categoria="Brasileira",
        )
        restaurante_criado = Mock(spec=RestauranteModel)

        criar_dao = Mock(return_value=restaurante_criado)
        monkeypatch.setattr(restaurante_service.restaurante_dao, "criar", criar_dao)
        resultado = restaurante_service.criar(sessao, dados)

        modelo = criar_dao.call_args.args[1]
        assert resultado is restaurante_criado
        assert isinstance(modelo, RestauranteModel)
        assert modelo.nome == dados.nome
        assert modelo.rua == dados.rua
        assert modelo.bairro == dados.bairro
        assert modelo.numero == dados.numero
        assert modelo.cidade == dados.cidade
        assert modelo.categoria == dados.categoria
        criar_dao.assert_called_once_with(sessao, modelo)

    def test_listar_retorna_lista_do_dao(self, monkeypatch):
        sessao = Mock()
        restaurantes = [Mock(spec=RestauranteModel)]

        listar_dao = Mock(return_value=restaurantes)
        monkeypatch.setattr(restaurante_service.restaurante_dao, "listar", listar_dao)
        resultado = restaurante_service.listar(sessao)

        assert resultado is restaurantes
        listar_dao.assert_called_once_with(sessao)

    def test_buscar_restaurante_delega_ao_dao(self, monkeypatch):
        sessao = Mock()
        restaurante = Mock(spec=RestauranteModel)

        buscar_dao = Mock(return_value=restaurante)
        monkeypatch.setattr(
            restaurante_service.restaurante_dao,
            "buscar_restaurante",
            buscar_dao,
        )
        resultado = restaurante_service.buscar_restaurante(sessao, 7)

        assert resultado is restaurante
        buscar_dao.assert_called_once_with(sessao, 7)

    def test_alterar_retorna_none_quando_restaurante_nao_existe(self, monkeypatch):
        sessao = Mock()

        buscar_dao = Mock(return_value=None)
        alterar_dao = Mock()
        monkeypatch.setattr(
            restaurante_service.restaurante_dao,
            "buscar_restaurante",
            buscar_dao,
        )
        monkeypatch.setattr(restaurante_service.restaurante_dao, "alterar", alterar_dao)
        resultado = restaurante_service.alterar(
            sessao,
            7,
            RestauranteAlteracaoSchema(nome="Novo Nome"),
        )

        assert resultado is None
        buscar_dao.assert_called_once_with(sessao, 7)
        alterar_dao.assert_not_called()

    def test_alterar_atualiza_restaurante_com_dados_informados(self, monkeypatch):
        sessao = Mock()
        restaurante = Mock(spec=RestauranteModel)
        restaurante_atualizado = Mock(spec=RestauranteModel)
        dados = RestauranteAlteracaoSchema(nome="Novo Nome", numero=10)

        monkeypatch.setattr(
            restaurante_service.restaurante_dao,
            "buscar_restaurante",
            Mock(return_value=restaurante),
        )
        alterar_dao = Mock(return_value=restaurante_atualizado)
        monkeypatch.setattr(restaurante_service.restaurante_dao, "alterar", alterar_dao)
        resultado = restaurante_service.alterar(sessao, 7, dados)

        assert resultado is restaurante_atualizado
        alterar_dao.assert_called_once_with(
            sessao,
            restaurante,
            {"nome": "Novo Nome", "numero": 10},
        )

    def test_excluir_retorna_none_quando_restaurante_nao_existe(self, monkeypatch):
        sessao = Mock()

        buscar_dao = Mock(return_value=None)
        excluir_dao = Mock()
        monkeypatch.setattr(
            restaurante_service.restaurante_dao,
            "buscar_restaurante",
            buscar_dao,
        )
        monkeypatch.setattr(restaurante_service.restaurante_dao, "excluir", excluir_dao)
        resultado = restaurante_service.excluir(sessao, 7)

        assert resultado is None
        buscar_dao.assert_called_once_with(sessao, 7)
        excluir_dao.assert_not_called()

    def test_excluir_rejeita_restaurante_com_pedidos(self, monkeypatch):
        sessao = Mock()
        restaurante = Mock(spec=RestauranteModel)
        restaurante.pedidos = [Mock(spec=PedidoModel)]

        monkeypatch.setattr(
            restaurante_service.restaurante_dao,
            "buscar_restaurante",
            Mock(return_value=restaurante),
        )
        excluir_dao = Mock()
        monkeypatch.setattr(restaurante_service.restaurante_dao, "excluir", excluir_dao)
        with pytest.raises(HTTPException) as excecao:
            restaurante_service.excluir(sessao, 7)

        assert excecao.value.status_code == status.HTTP_409_CONFLICT
        assert excecao.value.detail == "Esse restaurante possui pedidos associados a ele"
        excluir_dao.assert_not_called()

    def test_excluir_remove_restaurante_sem_pedidos(self, monkeypatch):
        sessao = Mock()
        restaurante = Mock(spec=RestauranteModel)
        restaurante.pedidos = []

        monkeypatch.setattr(
            restaurante_service.restaurante_dao,
            "buscar_restaurante",
            Mock(return_value=restaurante),
        )
        excluir_dao = Mock()
        monkeypatch.setattr(restaurante_service.restaurante_dao, "excluir", excluir_dao)
        resultado = restaurante_service.excluir(sessao, 7)

        assert resultado is restaurante
        excluir_dao.assert_called_once_with(sessao, restaurante)
