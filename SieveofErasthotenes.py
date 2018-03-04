import math

def sito(koniec):
    k=2
    lista=[]
    for i in range(0,koniec+1,1):
        lista.append(i)   
    for i in range(2,int(math.ceil(math.sqrt(koniec)))+1,1):
        if lista[i]!=0:
            while k*i<=koniec:
                lista[k*i]=0
                k=k+1
        k=2
        
    print("Liczby pierwsze z zadanego przedzialu:")
    
    for i in range(0,len(lista),1):
        if lista[i]!=0:
            print(lista[i])
        
koniec=int(input("Podaj koniec przedzialu:"))
sito(koniec)

