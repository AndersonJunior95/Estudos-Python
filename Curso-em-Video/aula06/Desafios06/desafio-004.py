# O desafio propos que leia algo pelo teclado e mostra na trla o seu tipo primitivo e todas as informações possíveis sobre ele.
ler = input("Digite algo: ")

print ('A palavra digitada foi: {}'.format(ler))

print('O tipo primitivo de é {}'.format(type(ler)))
print ('Está escrito em minúsculo? {} '.format(ler.islower()))
print('É um número? {}'.format(ler.isnumeric()))
print('Está escrito em maiúsculo? {}'.format(ler.isupper()))
print('A palavra está captalizada? {}'.format(ler.istitle()))