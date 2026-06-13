from fastapi import FastAPI

from app.banco_de_dados import (
    base,
    engine
)
from app.routes.restaurante_routes import router_restaurantes

base.metadata.create_all(bind=engine)

# API Server Delivery
api = FastAPI(title="API Server Delivery")
api.include_router(router_restaurantes)

# Decorator: maneira de adicionar informações
# e comportamentos especiais a uma função.
@api.get("/")
def raiz():
    resposta = "Essa é a raiz da aplicação"
    return resposta