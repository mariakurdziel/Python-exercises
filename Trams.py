
def tramwaje(kod1,kod2):
    lista1=[]
    lista2=[]
    for i in range (0,len(kod1)-2):
        if ord(kod1[i])>64 and ord(kod1[i])<91 and int(kod1[i+1])>=0 and int(kod1[i+1])<=9 and ord(kod1[i+2])>64 and ord(kod1[i+2])<91:
            licz=int(kod1[i+1])
            for j in range(0,licz):
                lista1.append(kod1[i])
    if ord(kod1[len(kod1)-2])>64 and ord(kod1[len(kod1)-2])<91 and int(kod1[len(kod1)-1])>=0 and int(kod1[len(kod1)-1])<=9:
        licz=int(kod1[len(kod1)-1])
        for j in range(0,licz):
            lista1.append(kod1[len(kod1)-2])
                
    for i in range (0,len(kod2)-2):
        if ord(kod2[i])>64 and ord(kod2[i])<91 and int(kod2[i+1])>=0 and int(kod2[i+1])<=9 and ord(kod2[i+2])>64 and ord(kod2[i+2])<91:
            licz=int(kod2[i+1])
            for j in range(0,licz):
                lista2.append(kod2[i])
    if ord(kod2[len(kod2)-2])>64 and ord(kod2[len(kod2)-2])<91 and int(kod2[len(kod2)-1])>=0 and int(kod2[len(kod2)-1])<=9:
        licz=int(kod2[len(kod2)-1])
        for j in range(0,licz):
            lista2.append(kod2[len(kod2)-2])
            
    print(lista1)
    print(lista2)

    if len(lista1)>len(lista2):
        m=len(lista2)
    else:
        m=len(lista1)
        
    centrum=True   
    
    for i in range(0,m):
         if lista1[i]==lista2[i]:
             print("Tramwaje spotkaja sie na ulicy "+str(lista1[i])+" w "+str(i+1)+" minucie.")
             centrum=False
             break
         
    if centrum==True:
        print("Tramwaje spotykaja sie dopiero w centrum")
    
    
    
k1=str(input("Podaj kod 1 tramwaju:"))
k2=str(input("Podaj kod 2 tramwaju:"))

tramwaje(k1,k2)

