print(30*'=')
print('  Bem Vindo ao Zero cancela: ')
print(30*'=')


a = int(input("Digite um número: "))
a1 = 0 #Soma
a2 = 0 #Guarda anterior
considerados = 0
cont = 1

while a >= 0:
    #Soma total
    a1 = a1 + a

    if a == 0:
        if cont <= 2:
            #Desconsidera o Número
            a1 = a1 - a2
            if considerados == 0:
                considerados = 0
            else:
                considerados = +1
            cont = cont + 1
        else:
            print('Não pode ser colocado mais nenhum zero consecutivo!')  
    if a > 0:
        a2 = a
        considerados = considerados + 1
    a = int(input("Digite um número: "))



#Regra Número 3
else:
    print(30*'=')
    print('Game Over')
    print(f"Soma Total = {a1}")
    print(f"Números Considerados = {considerados}")
    print(f"Números Desconsiderados = {cont}")
    print(30*'=')  
