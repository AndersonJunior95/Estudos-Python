# Desafio proposto: Pegar as notas de aluno, P1 e P2, e verificar se ele está ou não de exame lembrando que para ele passar sem exame sua média precisa ser 7
# O clculo é P1 + P2 / 2
# Utilizando IF mostre se ele passou ou não

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