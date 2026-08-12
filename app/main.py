from fastapi import FastAPI
from app.routers.restaurante_router import router as router_restaurantes
from app.routers.pedido_router import router as router_pedidos
from app.banco_de_dados import modelo_base, localizador

modelo_base.metadata.create_all(bind=localizador)

# API Server Delivery
api = FastAPI(title="API Server Delivery")
api.include_router(router_restaurantes)
api.include_router(router_pedidos)

# Decorator: maneira de adicionar informações
# e comportamentos especiais a uma função.
@api.get("/")
def raiz():
    resposta = "Essa é a raiz da aplicação"
    return resposta