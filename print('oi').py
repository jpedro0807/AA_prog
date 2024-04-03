print(30*'=')
print('  Bem Vindo ao Zero cancela: ')
print(30*'=')


a = int(input("Digite um número: "))
a1 = 0 #Soma
a2 = 0 #Guarda anterior
considerados = 0
cont = 0
cont_desconsiderados = 0

while a >= 0:
    #Soma total
    a1 = a1 + a

    if a == 0:
        if cont < 3:
            #Desconsidera o Número
            a1 = a1 - a2
            considerados = considerados - 1
            cont = cont + 1
        else:
            print('Não pode ser colocado mais de 3 zeros consecutivos!')  
    if a > 0:
        a2 = a
        considerados = considerados + 1
        cont = 0
    a = int(input("Digite um número: "))




else:
    print(30*'=')
    print('Game Over')
    print(f"Soma Total = {a1}")
    print(f"Números Considerados = {considerados}")
    print(f"Números Desconsiderados = {cont}")
    print(30*'=')  
