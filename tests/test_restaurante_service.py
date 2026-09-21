from unittest.mock import Mock
from app.schemas.restaurante_schema import RestauranteCriacaoSchema
from app.models.restaurante_model import RestauranteModel
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
