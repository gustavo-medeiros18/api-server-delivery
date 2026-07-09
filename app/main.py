from fastapi import FastAPI
from app.routers.restaurante_router import router
from app.banco_de_dados import Base, engine

Base.metadata.create_all(bind=engine)

# API Server Delivery
api = FastAPI(title="API Server Delivery")
api.include_router(router)

# Decorator: maneira de adicionar informações
# e comportamentos especiais a uma função.
@api.get("/")
def raiz():
    resposta = "Essa é a raiz da aplicação"
    return resposta