# Desafio proposto pelo professor: Crie um programa que converta fahrenheit para celcius FORMULA (F - 32) * 5/9

fahrenheit = float(input("Digite a temperatura que deseja converter para celcius: "))

celcius = (fahrenheit - 32) * 5/9

print("A temperatura de {:.2f}ºF resultou em {:.2f}ºC".format(fahrenheit ,celcius))