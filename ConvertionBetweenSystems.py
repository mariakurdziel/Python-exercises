wynik=""
lista=[] 
wyraz=str(input("Podaj wyjsciowa liczbe:"))
sys1=int(input("System wyjsciowy:"))
sys2=int(input("System ostateczny:"))
dz=0
il=1
for i in range(len(wyraz)-1,-1,-1):
    if ord(wyraz[i])>64 and ord(wyraz[i])<71:
        dz=dz+il*(ord(wyraz[i])-55)
    else:
        dz=dz+int(wyraz[i])*il
    il=il*sys1;

while dz>0:
    reszta=dz%sys2
    if reszta>9:
        lista.append(str(chr(reszta+55)))
        dz=int(dz/sys2)
    else:
        lista.append(str(reszta))
        dz=int(dz/sys2)
        
lista.reverse()
for i in range(0,len(lista),1):
    wynik+=lista[i]        

print(wynik)
