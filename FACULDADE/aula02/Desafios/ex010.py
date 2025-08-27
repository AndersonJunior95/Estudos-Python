# A jornada de trabalho semanal de um funcionário é de 40 Horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cáclulo é o valor da hora regular com um acréscimo de 50%.

# Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas

valorHora = float(input("Digite o valor por Hra do funcionario: "))
horasTrabalhadas = int(input("Digite a quantidade de horas que o funcionário trabalhou: "))
salario = 0
salarioExtra = 0

if horasTrabalhadas-160 < 0:
    salario = horasTrabalhadas * valorHora
else: 
    salario = horasTrabalhadas * valorHora
    horasExtras = horasTrabalhadas - 160
    salarioExtra = salario + ((horasExtras * valorHora) * 0.50)
    salarioTotal = salarioExtra
print(f"O salário do funcionário é: {salarioTotal}")    

'''
hrTrabalhadas = int(input("Horas trabalhas: "))
slPHoras = int(input("Digite quanto ele ganha p/hora: "))


if hrTrabalhadas > 160:
    acrescimo = slPHoras * 1.50
    print(f"O acrescimo de horas extras foi de R${acrescimo:.2f}")
else: 
    print("Não fez horas extras")
'''