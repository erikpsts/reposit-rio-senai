'''
----------ENTRADA----------------
-   Ler três notas de um aluno
-   Ler o nome do Aluno
-   Ler o número da turma
----------PROCESSAMENTO----------
-   Calcular a média
-   Verificar status (média >= 70 é aprovado)
---------SAÍDA--------------
-   Mostrar a soma das notas
-   Mostrar a média das notas
-   Mostrar se foi "aprovado" ou "reprovado"
'''

nome = str(input("Digite o nome do aluno: "))
turma = int(input("Qual o número da turma?"))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

soma = n1 + n2 + n3

media = soma/3

print(f"A média do aluno é igual a: {media}")

if media >= 70: 
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado.")