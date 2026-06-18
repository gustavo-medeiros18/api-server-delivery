# nome_do_parametro: tipo_de_dados_especifico
def multiplicar_com_tipagem(x:int, y:int):
    multiplicacao = x * y
    return multiplicacao

resultado_1 = multiplicar_com_tipagem(10, 20)
print(f"Resultado 1 sem tipagem: {resultado_1}")

resultador_2 = multiplicar_com_tipagem("dev", "cdc")
print(f"Resultado 3 sem tipagem: {resultador_2}")