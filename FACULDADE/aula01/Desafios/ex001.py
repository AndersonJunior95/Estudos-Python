# Desafio proposto pelo professor: Criar uma calculadora que pegue dois dados armazenados por meio de perguntas do usuário e somar apresentando o valor (resultado) no terminal

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

s = n1 + n2

print ("A soma entre {} e {} deu: {}".format(n1, n2, s))