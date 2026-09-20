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