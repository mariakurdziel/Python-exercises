def cezarrozszyfr(kod, przesuniecie):
  for i in range (0, len(kod),1):
    if ord(kod[i])>96 and ord(kod[i])<123:
      var=chr(96+(((ord(kod[i])-96-przes)+26)%26))
      if var==chr(96):
        kod[i]=chr(122)
      else:
        kod[i]=var
  print(kod)
  
tekst=str(input("Podaj hasło do zaszyfrowania:"))
przes=int(input("Podaj przesuniecie:"))

lista=list(tekst)

for i in range (0,len(lista),1):
    if ord(lista[i])>64 and ord(lista[i])<91:
      lista[i]=chr(ord(lista[i])+32)

kod=cezarszyfr(lista,przes)
print(kod)
cezarrozszyfr(kod,przes)
