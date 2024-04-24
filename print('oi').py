print(30*'=')
print('  Bem Vindo ao Zero cancela: ')
print(30*'=')


a = int(input("Digite um número: "))
soma = 0 #Soma
a1 = 0 #Guarda anterior 1
a2 = 0 #Guarda anterior 2
a3 = 0 #Guarda anteterior 3

considerados = 0
cont_desconsiderados = 0
cont = 0 

while a >= 0:
    #Soma total
    soma += a
    
    #Desconsidera o Número
    if a == 0:
        if a1==0 and a2==0 and a3==0:
            cont = 1
            print('Não pode ser colocado mais de 3 zeros consecutivos!')

        soma = soma - a1
        considerados = considerados - 1
        
        a1 = a2 
        a2 = a3
        a3 = 0
        
        if cont == 1:
            cont_desconsiderados = cont_desconsiderados
            considerados = considerados + 1
        
        else:
            cont_desconsiderados = cont_desconsiderados + 1
        
        
        if a1 == 0:
            a1 = a2
            a2 = a3
            a3 = 0
            if a2 == 0:
                a2 = a3
                a3 = 0
        
    if a > 0:
        a3 = a2
        a2 = a1
        a1 = a
        considerados = considerados + 1
        cont = 0
        
    a = int(input("Digite um número: "))
    




else:
    print(30*'=')
    print('Game Over')
    print(30*'-')
    print(f"Soma Total = {soma}")
    print(f"Números Considerados = {considerados}")
    print(f"Números Desconsiderados = {cont_desconsiderados}")
    print(30*'=')  
