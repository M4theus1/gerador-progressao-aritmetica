c = 1
soma = 0
print('GERADOR DE PA')
print('=-'*15)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = n
while c <= 10:
    print(' {} ->'.format(termo), end='')
    termo += r
    c += 1
print('FIM')