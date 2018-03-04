def babelkowe(lista,k):
  licz=0

  while k>=2:
    for i in range (0,k-1,1):
        if(lista[i]>lista[i+1]):
            lista[i],lista[i+1]=lista[i+1],lista[i]
            licz=licz+1
    if licz==0:
      break
    else:
      k=k-1
      licz=0
  print(lista)
