from unittest.mock import Mock
from app.schemas.restaurante_schema import RestauranteCriacaoSchema
from app.models.restaurante_model import RestauranteModel

def test_criar():
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