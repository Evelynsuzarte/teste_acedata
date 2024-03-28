def exercicio1(salario_hora, horas_trabalhadas, n_filhos):
    salario_bruto = 0
    salario_familia = 0
    salario_liquido = 0

    salario_bruto = salario_hora*horas_trabalhadas
    if salario_bruto <= 788:
        salario_familia = 30.50*n_filhos
        salario_liquido = salario_bruto+salario_familia
    
    elif salario_bruto > 788 and salario_bruto >= 1100:
        salario_familia = 18.50*n_filhos
        salario_liquido = salario_bruto+salario_familia
    
    elif salario_bruto > 1100:
        salario_familia = 11.90*n_filhos
        salario_liquido = salario_bruto+salario_familia
    
    print(f"Exercício 1: Salário Bruto = R${salario_bruto} / Salário Família = R${salario_familia} / Salário Líquido = R${salario_liquido}")
    
def exercicio2(n, sequencia):
    maior = sequencia[0]
    menor = sequencia[0]

    for i in range(n):
        if sequencia[i] > maior:
            maior = sequencia[i]
    
    for i in range(n):
        if sequencia[i] < menor:
            menor = sequencia[i]

    print(f"\nExercício 2: Sequência - {sequencia}\nMaior = {maior} - Menor = {menor}")


def exercicio3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return exercicio3(n-1) + exercicio3(n-2)

#exercicio1(17.50, 40, 2)
#exercicio2(5, [28,78,19,47,46])
print(exercicio3(10))
