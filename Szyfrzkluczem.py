def szyfrklucz(klucz,napis):
  m=0
  for i in range(0,len(napis),1):
    if ord(napis[i])>96 and ord(napis[i])<123:
      var=chr(96+((ord(napis[i])-96+klucz[m])%26))
      if var==chr(96):
        napis[i]=chr(122)
      else:
        napis[i]=var
      m=m+1
    if m==len(klucz)-1:
      m=0
  print(napis)
  return napis  
    
def rozszyfr(klucz, napis):
  m=0
  for i in range(0,len(napis),1):
    if ord(napis[i])>96 and ord(napis[i])<123:
      var=chr(96+(((ord(kod[i])-96-klucz[m])+26)%26))
      if var==chr(96):
        kod[i]=chr(122)
      else:
        kod[i]=var
      m=m+1
    if m==len(klucz)-1:
      m=0
  print(napis)
  
napis=str(input("Podaj haslo do zaszyfrowania:"))
klucz=str(input("Podaj klucz"))

napis=list(napis)

for i in range (0,len(napis),1):
    if ord(napis[i])>64 and ord(napis[i])<91:
      napis[i]=chr(ord(napis[i])+32)
      
klucz=list(klucz)
kluczl=[]
for i in range(0,len(klucz),1):
  kluczl.append(ord(klucz[i])-96)
  
kod=szyfrklucz(kluczl,napis)
rozszyfr(kluczl,kod)
