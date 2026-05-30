from fastapi import FastAPI

from app.routes.restaurante_routes import router_restaurantes

app = FastAPI(
    title="API Delivery"
)
app.include_router(router_restaurantes)

@app.get("/")
def inicio():
    resposta = {
        "mensagem": "API Delivery funcionando"
    }
    
    return resposta