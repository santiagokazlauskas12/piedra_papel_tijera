import random


#-------------------------------------------------------------------------------
def juego (x,y):
    if x == y:
        return(" Empate !")

    elif x%2 and y%2 ==1:
        return(min(x,y))
       
    else:
        return(max(x,y))  
#-------------------------------------------------------------------------------
lista = ["piedra", "papel", "tijera"]
x=None
while x not in lista:    
    x=input(""" elije :
                
                    -piedra
                    -papel
                    -tijera
                
-recuerda que debes escribirlo igual    
                 
                    -""")


select={"piedra":1,"papel":2,"tijera":3}
cpu=[1,2,3]
random.shuffle(cpu)
player=select[x]
lista = ["piedra", "papel", "tijera"]

print("Player elige : {}, la cpu {}".format(x,lista[cpu[0]-1]))

if player == cpu[0]:
    print( "Empate ! ")
else:
    ganador=juego(player,cpu[0])
    if ganador == player:
        print ("Tu eres el ganador !")
    else:
        print( " Perdiste !")