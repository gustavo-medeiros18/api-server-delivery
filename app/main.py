from fastapi import FastAPI

from app.routes.restaurante_routes import router_restaurantes

# API Server Delivery
api = FastAPI(title="API Server Delivery")
api.include_router(router_restaurantes)

# Decorator: maneira de adicionar informações
# e comportamentos especiais a uma função.
@api.get("/")
def raiz():
    resposta = "Essa é a raiz da aplicação"
    return resposta