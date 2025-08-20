# Desafio proposto pelo professor: Crie um programa que leia o salario mensal de um funcionario e calcula o percentual de ajuste

salario = float(input("Digite o salário fixo do funcionário: "))

ajuste = (salario / 100) * 20   # Ou salario * 1.2

fixo = salario + ajuste

print("O aumento na folha salarial do funcionário será de R${}".format(ajuste))
print("O salário bruto do funcionário será: R${:.2f}".format(fixo))