#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 01:55:45 2017

@author: maria
"""

class Node:
 
    def __init__(self, name,grade):
        self.name = name
        self.grade = grade
        self.next = None

    def __str__(self):
        return str(self.name)+" "+str(self.grade)
 
class Onedirectional():
    
    def __init__(self):
        self.head=None
        self.counter=0
        
    def add_beg(self,name,grade):
        new=Node(name,grade)
        
        if not self.head:
            self.head=new
        else:
            new.next=self.head
            self.head=new
        self.counter+=1

    
    def add_last(self,name,grade):
        new=Node(name,grade)
        if not self.head:
            self.head=new
        else:
            wsk=self.head
            while wsk.next:
                wsk=wsk.next
            wsk.next=new
        self.counter=self.counter+1
    
    def add_n(self,name,grade,n):
        new=Node(name,grade)
        licz=1
        if self.counter==0:
            self.head=new
        else:
            if n==1:
                Onedirectional().add_beg(name,grade) 
            elif n==self.counter+1:
                Onedirectional().add_last(name,grade)
            elif n>self.counter+1:
                print("Za daleka pozycja!!!")
            else:
                wsk=self.head
                while licz<n:
                    licz=licz+1
                    o=wsk
                    wsk=wsk.next
                o.next=new
                new.next=wsk

    def delete_first(self):
        if self.counter==0:
            print("Lista już jest pusta!")
        elif self.counter==1:
            self.head=None
        else:
            self.head=self.head.next
        self.counter=self.counter-1
            
    def delete_last(self):
        n=None
        wsk=self.head
        if self.counter==0:
            print("Lista już jest pusta!")
        elif self.counter==1:
            self.head=None
        else:
            while wsk.next.next:
                wsk=wsk.next
            wsk.next=None
        self.counter=self.counter-1

    def printlist(self):
        wsk=self.head
        
        while wsk:
            print(wsk)
            wsk=wsk.next
    
    def best_grade(self):
        lista=[]
        wsk=self.head
        max=0
        if self.counter==1:
            print(self.head)
        else:
            while wsk:
                if wsk.grade>max:
                    max=wsk.grade
                wsk=wsk.next
            wsk=self.head
            while wsk:
                if wsk.grade==max:
                    lista.append(wsk.name)
                wsk=wsk.next
            print ("Najlepszy wynik kolokwium to "+str(max))
            print ("Osoby o powyższym wyniku:")
            for i in range(0,len(lista),1):
                print(lista[i])
                
            

                
nazwiska=["Nowak","Kowalski", "Kleczek","Godyn", "Kurdziel", "Zajac","Sokol", "Chlebicka","Musial","Rapacz"]  
oceny=[8,16,40,29,15,17,39,25,40,24]   

fun = Onedirectional()

for i in range(0,10,1):
    fun.add_last(nazwiska[i],oceny[i])  

print("Początkowy stan listy:\n")
fun.printlist()
print("\n")                  
print("Po dodaniu jednego elementu na początku:\n")
fun.add_beg("Kaplon",25)
fun.printlist()
print("\n")
print("Po dodaniu jednego elementu na koncu:\n")
fun.add_last("Sarnek",19)
fun.printlist()
print("\n")      
print("Po dodaniu jednego elementu na pozycji n:\n")
fun.add_n("Wozniak",14,1)
fun.printlist()
print("Po usunieciu pierwszego elementu:\n")
fun.delete_first()
fun.printlist()
print("\n")
print("Po usunieciu ostatniego elementu:\n")
fun.delete_last()
fun.printlist()
print("\n")   
fun.best_grade()
