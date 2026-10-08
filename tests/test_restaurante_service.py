from unittest.mock import Mock
from pytest import raises
from fastapi import HTTPException, status
from app.schemas.restaurante_schema import RestauranteCriacaoSchema, RestauranteAlteracaoSchema
from app.models.restaurante_model import RestauranteModel
from app.models.pedido_model import PedidoModel
from app.services import restaurante_service

def test_criar(monkeypatch):
    dados_entrada_exemplo = RestauranteCriacaoSchema(
        nome="Restaurance Central",
        rua="Rua do parque",
        bairro="Centro",
        numero=123,
        cidade="São Paulo",
        categoria="Comida brasileira"
    )

    sessao_simulada = Mock()
    retorno_dao_simulada = Mock(spec=RestauranteModel)
    criar_dao_simulado = Mock(return_value=retorno_dao_simulada)

    monkeypatch.setattr(restaurante_service.restaurante_dao, "criar", criar_dao_simulado)

    resultado = restaurante_service.criar(sessao_simulada, dados_entrada_exemplo)

    modelo_dados_criado = criar_dao_simulado.call_args.args[1]

    assert resultado is retorno_dao_simulada
    assert isinstance(modelo_dados_criado, RestauranteModel)
    assert modelo_dados_criado.nome == dados_entrada_exemplo.nome
    assert modelo_dados_criado.rua == dados_entrada_exemplo.rua
    assert modelo_dados_criado.bairro == dados_entrada_exemplo.bairro
    assert modelo_dados_criado.numero == dados_entrada_exemplo.numero
    assert modelo_dados_criado.cidade == dados_entrada_exemplo.cidade
    assert modelo_dados_criado.categoria == dados_entrada_exemplo.categoria

    criar_dao_simulado.assert_called_with(sessao_simulada, modelo_dados_criado)

def test_listar(monkeypatch):
    sessao_simulada = Mock()

    retorno_dao_simulado = Mock(spec=RestauranteModel)
    lista_simulada = [retorno_dao_simulado]

    listar_dao_simulado = Mock(return_value=lista_simulada)
    monkeypatch.setattr(restaurante_service.restaurante_dao, "listar", listar_dao_simulado)

    resultado = restaurante_service.listar(sessao_simulada)

    assert resultado is lista_simulada
    listar_dao_simulado.assert_called_with(sessao_simulada)

def test_buscar(monkeypatch):
    sessao_simulada = Mock()

    retorno_dao_simulado = Mock(spec=RestauranteModel)
    buscar_dao_simulado = Mock(return_value=retorno_dao_simulado)

    monkeypatch.setattr(restaurante_service.restaurante_dao, "buscar_restaurante", buscar_dao_simulado)

    resultado = restaurante_service.buscar_restaurante(sessao_simulada, 7)

    assert resultado is retorno_dao_simulado
    buscar_dao_simulado.assert_called_with(sessao_simulada, 7)

def test_excluir_restaurante_sem_pedidos(monkeypatch):
    sessao_simulada = Mock()

    retorno_dao_simulado = Mock(spec=RestauranteModel)
    retorno_dao_simulado.pedidos = []

    buscar_dao_simulado = Mock(return_value=retorno_dao_simulado)
    monkeypatch.setattr(restaurante_service.restaurante_dao, "buscar_restaurante", buscar_dao_simulado)

    excluir_dao_simulado = Mock()
    monkeypatch.setattr(restaurante_service.restaurante_dao, "excluir", excluir_dao_simulado)

    resultado = restaurante_service.excluir(sessao_simulada, 7)

    assert resultado is retorno_dao_simulado
    excluir_dao_simulado.assert_called_with(sessao_simulada, retorno_dao_simulado)

def test_excluir_restaurante_retorna_none(monkeypatch):
    sessao_simulada = Mock()

    retorno_dao_simulado = None
    buscar_dao_simulado = Mock(return_value=retorno_dao_simulado)
    monkeypatch.setattr(
        restaurante_service.restaurante_dao,
        "buscar_restaurante",
        buscar_dao_simulado
    )

    excluir_dao_simulado = Mock()
    monkeypatch.setattr(
        restaurante_service.restaurante_dao,
        "excluir",
        excluir_dao_simulado
    )

    resultado = restaurante_service.excluir(sessao_simulada, 7)

    assert resultado == None
    buscar_dao_simulado.assert_called_with(sessao_simulada, 7)
    excluir_dao_simulado.assert_not_called()

def test_excluir_restaurante_lanca_excecao(monkeypatch):
    sessao_simulada = Mock()

    retorno_dao_simulado = Mock(spec=RestauranteModel)
    pedido_simulado = Mock(spec=PedidoModel)
    retorno_dao_simulado.pedidos = [pedido_simulado]
    buscar_dao_simulado = Mock(return_value=retorno_dao_simulado)

    monkeypatch.setattr(
        restaurante_service.restaurante_dao,
        "buscar_restaurante",
        buscar_dao_simulado
    )

    excluir_dao_simulado = Mock()
    monkeypatch.setattr(
        restaurante_service.restaurante_dao,
        "excluir",
        excluir_dao_simulado
    )

    excecao_capturada = raises(
        HTTPException,
        restaurante_service.excluir,
        sessao_simulada,
        7
    )

    assert excecao_capturada.value.status_code == status.HTTP_409_CONFLICT
    assert excecao_capturada.value.detail == "Esse restaurante possui pedidos associados a ele"
    excluir_dao_simulado.assert_not_called()

def test_alterar_restaurante_com_exito(monkeypatch):
    sessao_simulada = Mock()

    retorno_buscar_dao_simulado = Mock(spec=RestauranteModel)
    buscar_dao_simulado = Mock(return_value=retorno_buscar_dao_simulado)

    monkeypatch.setattr(
        restaurante_service.restaurante_dao,
        "buscar_restaurante",
        buscar_dao_simulado
    )

    retorno_alterar_dao_simulado = Mock(spec=RestauranteModel)
    alterar_dao_simulado = Mock(return_value=retorno_alterar_dao_simulado)

    monkeypatch.setattr(
        restaurante_service.restaurante_dao,
        "alterar",
        alterar_dao_simulado
    )

    dados_entrada_exemplo = RestauranteAlteracaoSchema(
        nome="Novo nome do restaurante",
        rua="Nova rua do restaurante"
    )

    resultado = restaurante_service.alterar(sessao_simulada, 7, dados_entrada_exemplo)

    assert resultado is retorno_alterar_dao_simulado
    alterar_dao_simulado.assert_called_with(
        sessao_simulada,
        retorno_buscar_dao_simulado,
        {"nome": "Novo nome do restaurante", "rua": "Nova rua do restaurante"}
    )
