# desafio-
'''
    Elabore um programa que leia um número
    Verifique se o número é par ou ímpar
    E mostre a mensagem na tela
        "É par" ou "É impar"

'''

numero = int(input("Digite um número: "))

if numero%2 == 0: 
    print(f"O número {numero} é par")
else: 
    print(f"O número {numero} é ímpar")
    
# se um número não é par automaticamente é impar.