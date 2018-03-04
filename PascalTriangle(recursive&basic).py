def pasi(h)
    wiersz=""
    licz=2
    ogr1=h
    lista1=[]
    lista2=[]
    
    for i in range (1,2*h,1):
    	if i==ogr1:
    		wiersz+="1"
    		lista1.append(1)
    	wiersz+=" "
    	lista1.append(0)
    	
    print (wiersz)
    ogr1=ogr1-1
    ogr2=ogr1+2
    wiersz=""
    
    while licz<=h:
    	for i in range (1,ogr1,1):
    		wiersz+=" "
    		lista2.append(0)
    	wiersz+="1"
    	lista2.append(1)
    	w=ogr1+1
    	while w<ogr2:
    		if w<ogr2:
    			wiersz+=" "
    			lista2.append(0)
    			w=w+1
    		else:
    			break
    		if w<ogr2:
    			x=lista1[w-2]
    			y=lista1[w]
    			wyr=x+y
    			wiersz+=str(wyr)
    			lista2.append(wyr)
    			w=w+1
    		else:
    			break
    	wiersz+="1"
    	lista2.append(1)
    	
    	for i in range (ogr2+1,2*h,1):
    		wiersz+=" "
    		lista2.append(0)
    	
    	print (wiersz)
    	licz=licz+1
    	wiersz=""
    	ogr1=ogr1-1
    	ogr2=ogr2+1
    	
    	for i in range (0, 2*h-1,1):
    		lista1[i]=lista2[i]
    	lista2=[]

def pascalr(w,k):
	if w==0 or k==0 or w==k:
	  return 1
	else:
	  return pascal(w-1,k)+pascal(w-1,k-1)
		
h=int(input("Podaj wysokosc:\n"))
pasi(h)

	  
tab=[]
for i in range(0,n+1):
  for j in range(0,i+1):
    tab.append(pascalr(i,j))
  print(tab)
  tab=[]
