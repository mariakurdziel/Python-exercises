def iks(x):
    
    promien=int(x/2)
    licz=0
    tab=['.']*x
    for i in range(x):
      tab[i]=['.']*x

    if x%2==0:
        sr=int(x/2)
    else:
        sr=int((x-1)/2)
        
    while True:            
        if x%2==1:
            for a in range(0,promien+1):
                for i in range(x):
                    for j in range(x):
                        if abs(j-sr)==a and abs(i-sr)==a:
                            tab[i][j]="x"
                for i in range(x):
                    print("".join (tab[i]))
                print("\n")
                
            for a in range(promien,-1,-1):
                for i in range(x):
                    for j in range(x):
                        if abs(j-sr)==a and abs(i-sr)==a:
                            tab[i][j]="."
                for i in range(x):
                    print("".join(tab[i]))
                print("\n")
        else:
            tab[sr][sr]="x"
            tab[sr][sr-1]="x"
            tab[sr-1][sr-1]="x"
            tab[sr-1][sr]="x"
            
            for i in range(x):
                    print("".join (tab[i]))
            
            promien=int((x-2)/2)
    
            for k in range(1,promien+1):
                tab[sr+k][sr+k]="x"
                tab[sr+k][sr-1-k]="x"
                tab[sr-1-k][sr-1-k]="x"
                tab[sr-1-k][sr+k]="x"
                
                for i in range(x):
                    print("".join (tab[i]))
            
            for k in range(promien,0,-1):
                tab[sr+k][sr+k]="."
                tab[sr+k][sr-1-k]="."
                tab[sr-1-k][sr-1-k]="."
                tab[sr-1-k][sr+k]="."
                
                for i in range(x):
                    print("".join (tab[i]))
                    
            tab[sr][sr]="."
            tab[sr][sr-1]="."
            tab[sr-1][sr-1]="."
            tab[sr-1][sr]="."
            
            for i in range(x):
                    print("".join (tab[i]))
iks(8)

