# Desafio proposto: Ler duas notas fornecidas pelo usuário, calcular a média aritmética entre elas e exibir o resultado de forma formatada.

n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))

media = (n1 + n2) / 2

print("A média entre {} e {} é igual a {}".format(n1, n2, media))