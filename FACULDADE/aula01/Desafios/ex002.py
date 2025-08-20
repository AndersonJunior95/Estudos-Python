# Desafio proposto pelo professor: Fazer um programa que calcule a altura e a base e apresenta a área no terminal

altura = float(input("Digite a altura: "))
base = float(input("Digite a base: "))

calculo = altura * base

print ("Dado a Altura {} e a Base {} obtivemos {:.2f} de área".format(altura, base, calculo))