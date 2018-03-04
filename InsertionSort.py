def wstawianie(lista,n):
  for i in range(0,n,1):
    k=i
    while k>=1 and lista[k-1]>lista[i]:
      k=k-1
    if k!=i:
      tmp=lista[i]
      for j in range (i,k,-1):
        lista[j]=lista[j-1]
      lista[k]=tmp
  print(lista)    
