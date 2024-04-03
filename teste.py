print(30*'=')
print('Bem Vindo ao Zero cancela: ')
print(30*'=')
n = int(input('Digite seu Número: '))
# s = soma
s = 0
# cons = numeros considerados
cons = 0
desc = 0
cont = 0
while n >= 0:
    if n > 0:
        s += n
        cons = +1
    else:
        desc = +1
        cont = +1
    n = int(input('Digite seu Número: '))
if n == 0:
    print(f'numeros desconsiderados sao {desc}')
    print(f'soma = {s}')
    print(f'numeros considerados {cons}')









print(f'numeros desconsiderados sao {desc}')
print(f'soma = {s}')
print(f'numeros considerados {cons}')

