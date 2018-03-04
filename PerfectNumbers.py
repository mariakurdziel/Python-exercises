def doskonale(n):
    sumal=1
    for i in range (3,n+1,1):
       for j in range (2,int(math.sqrt(i))+1,1):
           if i%j==0:
               sumal+=j+(i/j)
       if sumal==i:
               print(i)
       sumal=1

n=int(input("Podaj zakres:"))           
print("Liczby doskonale:")
doskonale(n)

