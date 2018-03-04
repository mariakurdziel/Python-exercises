def szyfrpodst(szyfr,napis):
  for i in range(0, len(napis),1):
    if ord(napis[i])>96 and ord(napis[i])<123:
      napis[i]=szyfr[ord(napis[i])-97]
  print(napis)
  print("\n")
  return napis  

def rozszyfrpodst(szyfr, napis):
  for i in range(0, len(napis),1):
    for j in range(0,len(szyfr),1):
      if napis[i]==szyfr[j]:
        napis[i]=chr(97+j)
        break
  print(napis)
  

alfabet="abcdefghijklmnopqrstuvwxyz"
alfabet=list(alfabet)
szyfr=[]

napis=str(input("Napis do zaszyfrowania:"))
napis=list(napis)

for i in range (0,len(napis),1):
    if ord(napis[i])>64 and ord(napis[i])<91:
      napis[i]=chr(ord(napis[i])+32)

while len(alfabet)>0:
  x=random.randint(0,len(alfabet)-1)
  szyfr.append(alfabet[x])
  alfabet.remove(alfabet[x])

print(szyfr)
print("\n")

kod=szyfrpodst(szyfr,napis)
rozszyfrpodst(szyfr,kod)
