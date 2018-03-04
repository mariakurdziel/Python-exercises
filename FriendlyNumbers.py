def sumdziel(x):
    sumad=1
    for j in range (2,int(math.sqrt(x))+1,1):
           if x%j==0:
               sumad+=j+int(x/j)
    return sumad

def zaprzyjaznione(n):
    lista=[]

    for i in range(0,n+1):
        lista.append(i)
        
    for i in range(0,len(lista)):
        if lista[i]!=0:        
            x=sumdziel(lista[i])
            y=sumdziel(x)
            if y==lista[i] and x!=lista[i]:
                print("Liczby "+str(y)+ " i "+str(x)+ " to liczby zaprzyjaznione")
                lista[x]=0

n=int(input("Podaj zakres:"))  
