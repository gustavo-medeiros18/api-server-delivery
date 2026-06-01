from fastapi import FastAPI

from app.routes.restaurante_routes import router_restaurantes

api = FastAPI(
    title="API Delivery"
)
api.include_router(router_restaurantes)

@api.get("/")
def raiz():
    resposta = "API Delivery funcionando"
    
    return resposta