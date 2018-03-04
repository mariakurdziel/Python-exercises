def wybieranie(lista,roz):
  k=0
  min=roz
  minind=0 
  while k<roz:
    for i in range(k,roz,1):
      if lista[i]<min:
        min=lista[i]
        minind=i
    lista[minind]=lista[k]
    lista[k]= min
    k=k+1
    min=roz
  print(lista)

