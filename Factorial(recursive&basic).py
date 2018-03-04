import time
start_time = time.time()


def silniar(n):
    if n<2:
        return 1
    else:
        return n*silniar(n-1)
        

def silniai(n):
    if n==0:
        return 1
    il=1
    for i in range (1,n+1,1):
        il=il*i
    return il
    
n=int(input("Podaj liczbe n"))
x=silniai(n)
print("Silnia dla danej liczby wynosi:"+str(x))
y=silniar(n)
print("Silnia dla danej liczby wynosi:"+str(y))
print("--- %s seconds ---" % (time.time() - start_time))

