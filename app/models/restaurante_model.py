from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import Column, Integer, String
from app.banco_de_dados import base

def agora_iso():
    return (
        datetime.now(ZoneInfo("America/Sao_Paulo"))
        .replace(microsecond=0)
        .strftime("%Y-%m-%dT%H:%M:%S")
    )

class Restaurante(base):
    __tablename__ = "restaurantes"
    
    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)
    rua = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    cidade = Column(String, nullable=False)
    categoria = Column(String, nullable=False)

    created_at = Column(
        String,
        default=agora_iso,
    )

    updated_at = Column(
        String,
        default=agora_iso,
        onupdate=agora_iso
    )
