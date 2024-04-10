print(30*'=')
print('  Bem Vindo ao Zero cancela: ')
print(30*'=')


a = int(input("Digite um número: "))
soma = 0 #Soma
a1 = 0 #Guarda anterior 1
a2 = 0 #Guarda anterior 2
a3 = 0 #Guarda anteterior 3

considerados = 0
cont = 0
cont_desconsiderados = 0

while a >= 0:
    #Soma total
    soma += a
    print(f'a = {a}')
    if a == 0:
        a3 = a2
        a2 = a1
        a1 = a
        print(f'cont = {cont}')
        if cont < 3: #ERRO!!
            #Desconsidera o Número
            soma = soma - a1
            considerados = considerados - 1
            cont = cont + 1
            print(f'a1 = {a1}')
            print(f'a2 = {a2}')
            print(f'a3 = {a3}')
            print(f'soma = {soma}')
        if a1 == 0:
            a1 = a2
            a2 = a3
            a3 = 0
            if a2 == 0:
                a2 = a3
                a3 = 0
            print(f'a1 = {a1}')
            print(f'a2 = {a2}')
            print(f'a3 = {a3}')
            print(f'soma = {soma}')
    
        else:
            print('Não pode ser colocado mais de 3 zeros consecutivos!')
            print(f'a1 = {a1}')
            print(f'a2 = {a2}')
            print(f'a3 = {a3}')  
    if a > 0:
        a3 = a2
        a2 = a1
        a1 = a
        considerados = considerados + 1
        cont = 0
        print(f'a1 = {a1}')
        print(f'a2 = {a2}')
        print(f'a3 = {a3}')
        print(f'soma = {soma}')
    a = int(input("Digite um número: "))
    




else:
    print(30*'=')
    print('Game Over')
    print(f"Soma Total = {soma}")
    print(f"Números Considerados = {considerados}")
    print(f"Números Desconsiderados = {cont}")
    print(30*'=')  
