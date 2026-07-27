from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_BANCO = "sqlite:///./delivery.db"

localizador = create_engine(URL_BANCO)
fabrica_sessoes = sessionmaker(localizador)
modelo_base = declarative_base()

def obter_sessao():
    sessao_obtida = fabrica_sessoes()
    return sessao_obtida