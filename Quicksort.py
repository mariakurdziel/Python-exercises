def quicksort(lista,pocz,kon):
  piv=int((pocz+kon)/2)
  j=pocz
  lista[piv],lista[kon]=lista[kon],lista[piv]
  for i in range(pocz,kon,1):
    if lista[i]<=lista[kon]:
      lista[i],lista[j]=lista[j],lista[i]
      j+=1
  lista[j],lista[kon]=lista[kon],lista[j]
  if kon>j+1:
    quicksort(lista,j+1,kon)
  if pocz<j-1:
    quicksort(lista,pocz,j-1)
