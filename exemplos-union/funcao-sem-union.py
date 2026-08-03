# Nessa função, o valor passado como parâmetro só
# pode pertencer a um tipo de dados, que seria o
# tipo int.
def funcao_sem_union(numero: int):
    print(f"Parametro recebido pela função {numero}")

# Chamada sem nenhuma sinalização de erro. Tipagem
# do parâmetro está sendo respeitada.
funcao_sem_union(10)

# Tentar chamar a função passando o valor None,
# que não é um número inteiro (então não
# respeita a tipagem especificada no parâmetro),
# causará sinalização de erro de tipagem por
# parte do VS Code.
funcao_sem_union(None)