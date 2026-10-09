"""
-Crie um algorítmo que leia dois números
-Mostre no final qual número é o maior

------ENTRADA------
-Leia um número
-Leia outro número

------PROCESSAMENTO------
-veirificar quem é o maior

------Saída--------
-Mostrar o maior

"""

n1 = int(input("Digite o 1o número: "))
n2 = int(input("Digite o 2o número: "))

if n1 > n2:
    print(f"O número 1 ({n1}) é maior que o número 2 ({n2}). ")
elif n1 < n2:
    print(f"O número 1 ({n1}) é menor que o número 2 ({n2}). ")
else:
    print(f"O número 1 ({n1}) é igual ao número 2 ({n2}). ")