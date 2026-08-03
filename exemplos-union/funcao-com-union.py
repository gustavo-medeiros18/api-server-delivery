# Union é uma forma de especificar que um parâmetro (ou
# atributo de uma classe) pode pertencer a mais de um
# tipo de dados.

# A sintaxe geral para especificar que um parâmetro (ou
# atributo de uma classe) terá uma Union em sua tipagem
# é: nome_parametro: tipo_1 | tipo_2

# Nessa função, está sendo especificada uma union para
# o parâmetro recebido por ela. Aqui, o parâmetro
# recebido pode ser do tipo int ou então None.
def funcao_com_union(numero: int | None):
    print(f"Número recebido pela função {numero}")

# Chamada sem nenhuma sinalização de erro. Já que está
# sendo passado um número inteiro como parâmetro (que
# respeita a tipagem definida)
funcao_com_union(10)

# Passar None como um parâmetro agora não causa mais
# uma sinalização de erro. Já que None também é uma
# possibilidade de tipo graças a Union.
funcao_com_union(None)