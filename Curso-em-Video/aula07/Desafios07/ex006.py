# Desafio proposto: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input("Digite um número: "))

multiplica = n1 * 2
triplo = n1 * 3
raizQuadrada = n1 ** (1/2)

print ('O dobro de {} vale {}'.format(n1, multiplica))
print ('O triplo de {} vale {}'.format(n1, triplo))
print ('A raiz quadrada de {} vale {:.3}'.format(n1, raizQuadrada))