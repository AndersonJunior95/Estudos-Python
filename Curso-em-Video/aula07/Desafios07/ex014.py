# Desafio proposto: Escreva um programa que converta uma temperatura digitada em ºC e convertida para ºF

celcius = float(input("Informe a temperatura em ºC: "))

calculoF = (celcius * 9/5) + 32

print ("A temperatura de {}ºC convertido em Fahrenheit é {}ºF".format(celcius ,calculoF))