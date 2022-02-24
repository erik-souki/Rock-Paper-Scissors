import random


print('Pedra, Papel ou tesoura'+ '\n' +'vamos ver se vc tem sorte')

#Entrada da resposta do jogador
entrada = input('Manda a sua mão' + ' ').lower()

#Função pedra papel ou tesoura
def ppt(entrada):

    #Mãos válidas
    maos = ['pedra','papel','tesoura']

    #Mão aleatoria do programa
    aleatorio =  random.choice(maos)
    print("***" + aleatorio + "***")

    if entrada == aleatorio:
         return print('***Empate***')

    elif entrada == maos[0] and aleatorio == maos[1]:
        return print('***Você perdeu***')

    elif entrada == maos[0] and aleatorio == maos[2]:
        return print('***Você ganhou***')

    elif entrada == maos[1] and aleatorio == maos[0]:
         return print('***Você ganhou***')

    elif entrada == maos[1] and aleatorio == maos[2]:
        return print('***Você perdeu***')

    elif entrada == maos[2] and aleatorio == maos[0]:
        return print('***Você perdeu***')

    elif entrada == maos[2] and aleatorio == maos[1]:
        return print('***Você ganhou***')

    else:
        return print('Você precis mandar uma mão valida, pedra, papel e tesoura')
        

print(ppt(entrada))