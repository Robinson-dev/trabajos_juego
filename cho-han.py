import random as rd
billetera=1000000
gana=0
continuar ="si"
print(" ---Bienvenido a Cho Han (Par o Inpar)---")
print(f" usted tiene ${billetera}")
while billetera >0 and continuar=="si":
    apuesa =int(input(" Ingrese su apuesta : "))
    if apuesa<=billetera:
        dado1=rd.randint(1,6)
        dado2=rd.randint(1,6)
        total=dado1+dado2
        resto=total%2
        parinpar=input(" Adivina ¿ Par o Inpar ? ")
        print(f" Salió : {dado1} + {dado2} = {total}")
        if resto==0 and parinpar=="par":
            print(" ! Ganó ¡")
            billetera+=apuesa
            gana+=1
        elif resto!=0 and parinpar == "inpar":
            print(" ! Ganó ¡")
            billetera+=apuesa
            gana+=1
        else:
            print(" ! Perdió ¡")
            billetera-=apuesa
        print(f" Billetera: {billetera}")
        if billetera !=0:
            continuar= input(" Desea seguir jugando ?")
            print("-" *50)
        else:
            print(" La apuesta es mayor al dinero que tiene en la billetera")
print(f" usted gano {gana} partidas")
print(" Gracias por jugar...")
