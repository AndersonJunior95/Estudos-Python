# Desafio proposto: Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

n1 = int(input("Escreva um número: "))

ant = n1 - 1    # Cálculo para antecessor

suc = n1 + 1    # Cáculo para sucessor

print('O antecessor de {} é {} e o seu sucessor é {}'.format(n1, ant, suc))