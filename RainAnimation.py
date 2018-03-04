import random 
import os
import time
import sys

x=int(input("Podaj szerokosc planszy:"))
y=int(input("Podaj dlugosc planszy:"))
lista=y*[0]
wiersz=""
k=0
licz=0
  

for i in range(0,y,1):
        lista[i]=random.randrange(0,x-1)
        
while licz<5:
    for i in range(0,y,1):
        for i in range(0,lista[k],1):
            wiersz+="o"
        wiersz+="x"
        for i in range(lista[k]+1,x,1):
            wiersz+="o"      
        print(wiersz)
        wiersz=""
        k=k+1
    print("\n")
	time.sleep(0.3)
	os.system('cls')
    k=0
    z=random.randrange(0,x-1)
    for i in range(y-1,0,-1):
        lista[i]=lista[i-1]
    lista[0]=z
    licz=licz+1

