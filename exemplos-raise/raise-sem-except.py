while True:
    numero_lido = int(input("Digite um numero (para encerrar, digite 1000): "))

    if numero_lido == 1000:
        print("1000 digitado. Encerrando o programa")
        break
    elif numero_lido < 0:
        # O raise pode ser utilizado para lançar uma exceção
        # manualmente a partir de qualquer lugar do código.
        # Útil quando precisamos que seja disparada uma 
        # exceção em uma situação específica, que por si só
        # não representa exatamente um erro, mas que queremos
        # tratar como tal.

        # A sintaxe geral do raise é: raise <classe_da_excecao>

        # Como toda exceção disparada e que não é tratada por
        # uma cláusula try/except, o programa será interrompido
        # e a exceção será exibida no console.
        raise ValueError("O número não pode ser negativo")
