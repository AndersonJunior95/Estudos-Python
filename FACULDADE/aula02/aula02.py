# Condicionais

'''

numero = int(input("Digite um número: "))
if numero >= 100:
# if numero <= 100:
# if numero == 100:
# if numero != 100:
# if numero > 100:
# if numero < 100:
    print("Da não ta muito alto")

print(numero)

flag = False
if flag:
    print("A bandeira foi içada")
print("Esperando o próximo episodio")

'''

# Pegar 2 notas de aluno, P1

'''

print("="*20, "CALCULO DE MÉDIA", "="*20)

p1 = float(input("Digite a primeira nota do aluno \nNP1: "))
p2 = float(input("Digite a segunda nota do aluno \nNP2: "))

media = (p1 + p2) / 2

if media >= 7:
    print("="*20, "UUUUUHHHHUUUUUUUUUUUU", "="*20)
    
    print("Você passou direto!")
    print(f"A sua média foi: {media}")
else:
    print("="*20, "INFELIZMENTE", "="*20)
    print(f"Infelizmente! Você pegou exame\n Sua média foi {media}")
    
'''