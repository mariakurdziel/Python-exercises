def heapsort(tab):
  posortowana=[]

  def warunek(lista):
    for i in range(len(lista)-1,0,-1):
      if tab[i]>tab[math.floor((i-1)/2)]:
        tab[i],tab[math.floor((i-1)/2)]=tab[math.floor((i-1)/2)],tab[i]
    posortowana.append(lista[0])
    lista.pop(0)
    if len(lista)>=1:
      warunek(lista)
  warunek(lista)
  posortowana.reverse()
  print("Sortowanie kopcowe:\n", posortowana)
