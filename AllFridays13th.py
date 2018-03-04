
lista=[31,28,31,30,31,30,31,31,30,31,30,31]

r=2001
dzientyg=0
dzienm=0
liczG=0
k=0
while r<=2014:
    while k<12:
        mies=lista[k]
        while(dzienm<mies):
            dzienm+=1
            dzientyg+=1
            
            if dzientyg==5 and dzienm==13:
                liczG+=1
            
            if dzientyg==7:
                dzientyg=0
        dzienm=0
        k=k+1
    k=0
    if r%4==0:
        lista[1]=29
    else:
        lista[1]=28
    r=r+1
    
print("Liczba piatkow trzynastego w zadanym przedziale to"+ " "+str(liczG))
