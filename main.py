#questao 1
def exercicio1(salario_hora, horas_trabalhadas, n_filhos):
    salario_bruto = 0
    salario_familia = 0
    salario_liquido = 0

    salario_bruto = salario_hora*horas_trabalhadas

    if salario_hora < 0:
        return "Salario negativo"
    else:
        if salario_bruto <= 788.00:
            salario_familia = 30.50*n_filhos
            salario_liquido = salario_bruto+salario_familia
        
        elif salario_bruto > 788 and salario_bruto >= 1100:
            salario_familia = 18.50*n_filhos
            salario_liquido = salario_bruto+salario_familia
        
        elif salario_bruto > 1100:
            salario_familia = 11.90*n_filhos
            salario_liquido = salario_bruto+salario_familia
    
    #print(f"Exercício 1: Salário Bruto = R${salario_bruto} / Salário Família = R${salario_familia} / Salário Líquido = R${salario_liquido}")
    return f"Exercício 1: Salário Bruto = R${salario_bruto} / Salário Família = R${salario_familia} / Salário Líquido = R${salario_liquido}"

#questao 2
def exercicio2(n, sequencia):
    maior = sequencia[0]
    maior2 = 0
    menor = sequencia[0]

    for i in range(n):
        if sequencia[i] > maior:
            maior = sequencia[i]

    for i in range(n):
        if maior2 < maior and sequencia[i] < maior and sequencia[i] != maior and sequencia[i] > maior2 and maior!=maior2:
            maior2 = sequencia[i]

    for i in range(n):
        if sequencia[i] < menor:
            menor = sequencia[i]

    #print(f"\nExercício 2: Sequência - {sequencia}\nMaior = {maior} - Menor = {menor}")
    return f"Exercício 2: Sequência - {sequencia}\nMaior = {maior} - Menor = {menor} - Segundo maior = {maior2}"

#questao 3a
def exercicio3_a(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        sequencia = exercicio3_a(n - 1)
        posicao_ultimo = len(sequencia)
        if sequencia[posicao_ultimo-1] % 2 == 0:
            sequencia.append(sequencia[-1] + sequencia[-2] + sequencia[-3] )
        else:   
            sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia

#questao 3b
def exercicio3_b(n):
    lista = exercicio3_a(n)
    if n in lista:
        #print(f"O número {n} pertence a sequência Fibonacci.")
        return ("O número {n} pertence a sequência Fibonacci.")
    else:
        #print(f"O número {n} não pertence a sequência Fibonacci.")
        return f"O número {n} não pertence a sequência Fibonacci."



# exercicio1(17.50, 40, 2)
# exercicio2(5, [28,78,19,47,46])
# print("\nExercício 3: A sequência Fibonacci é :",exercicio3_a(10))
# exercicio3_b(10)

