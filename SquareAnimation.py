import math
import os
import sys

def kwadrat(w,k):


    if w>k:
    	promien=(k-1)/2
    	promien=int(promien)
    else:
    	promien=(w-1)/2
    	promien=int(promien)
    
    sr_kol=(k-1)/2
    sr_wier=(w-1)/2
    
    while True:
        for prom in range(0,promien+1):
        	for wier in range(0,w):
        		for kol in range(0,k):
        			if((abs(sr_kol-kol)==prom and abs(sr_wier-wier)<=prom) or (abs(srkol-kol)<=prom and abs(srwier-wier)==prom)):
        				sys.stdout.write("x")
        			else:
        				sys.stdout.write(".")
        		print()
        	print("------------------------------------------")
		
        
        for prom in range(promien-1,-1,-1):
        	for wier in range(0,w):
        		for kol in range(0,k):
        			if((abs(sr_kol-kol)==prom and abs(sr_wier-wier)<=prom) or (abs(srkol-kol)<=prom and abs(srwier-wier)==prom)):
        				sys.stdout.write("x")
        			else:
        				sys.stdout.write(".")
        		print()
        	print("------------------------------------------")
     
w=int(input("Podaj liczbę w"))
k=int(input("Podaj liczbę k"))

kwadrat(w,k)
