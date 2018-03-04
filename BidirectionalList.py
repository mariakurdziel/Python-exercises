# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
 
    def __init__(self, name,grade):
        self.name = name
        self.grade = grade
        self.next = None
        self.prev=None

        
class BidirectionalList:
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.counter=0
    
    def add_beg(self,name,grade):
        
        new=Node(name,grade)
        new.next=self.head
        self.head=new
        self.counter=self.counter+1
        
        if new.next:
            new.next.prev=new
        else:
            self.tail=new            
            
    def add_end(self,name,grade):
        
        new=Node(name,grade)
        new.prev=self.tail
        self.tail=new
        self.counter=self.counter+1
        
        if new.prev:
            new.prev.next=new
        else:
            self.head=new
    
    def add_n(self,name,grade,n):
        BidirectionalList()
        licz=1
        if self.counter==0:
            n=Node(name,grade)
            self.tail=n
            self.head=n
        else:
            if n==1:
                BidirectionalList.add_beg(self,name,grade)
            elif n==self.counter+1:
                BidirectionalList.add_end(self,name,grade)
            elif n>self.counter+1:
                print("Pozycja zbyt duża!")
            else:
                wsk=self.head
                while(licz<n):
                    wsk=wsk.next
                    licz=licz+1
                new=Node(name,grade)
                new.prev=wsk.prev
                new.next=wsk
                wsk.prev.next=new
                wsk.prev=new
            
    def delete_last(self):
        if self.counter==0:
            print("Lista jest pusta\n")
        elif self.counter==1:
            self.head=None
            self.tail=None
        else:
           self.tail=self.tail.prev
           self.tail.next=None
           self.counter=self.counter-1
        
    
    def delete_first(self):
        if self.counter==0:
            print("Lista jest pusta\n")
        elif self.counter==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            self.counter=self.counter-1

        
    def cross_list_from_beg(self):
        
        if not self.head:
            print("Lista pusta!")
        else:
            p=self.head
            while p:
                print(str(p.name)+" "+str(p.grade))
                p=p.next
                
    def cross_list_from_end(self):
        
        if not self.tail:
            print("Lista pusta!")
        else:
            p=self.tail
            while p:
                print(str(p.name)+" "+str(p.grade))
                p=p.prev
        
    def best_grade(self):
        max=0
        wsk=self.head
        if self.counter == 0:
            print("Lista jest pusta\n")
        else:
            while wsk:
                if wsk.grade>max:
                    max=wsk.grade
                    value=wsk.name
                wsk=wsk.next
            print(value)
            
nazwiska=["Nowak","Kowalski", "Kleczek","Godyn", "Kurdziel", "Zajac","Sokol", "Chlebicka","Musial","Rapacz"]  
oceny=[8,16,40,29,15,17,39,25,18,24]   

fun = BidirectionalList()

for i in range(0,10,1):
    fun.add_end(nazwiska[i],oceny[i])

print("Początkowy stan listy:\n")
fun.cross_list_from_beg()
print("\n")
print("Po dodaniu jednego elementu na początku:\n")
fun.add_beg("Kaplon",25)
fun.cross_list_from_beg()
print("\n")
print("Po dodaniu jednego elementu na koncu:\n")
fun.add_end("Sarnek",19)
fun.cross_list_from_beg()
print("\n")      
print("Po dodaniu jednego elementu na pozycji n:\n")
fun.add_n("Wozniak",14,6)
fun.cross_list_from_beg()
print("\n")
print("Po usunieciu pierwszego elementu:\n")
fun.delete_first()
fun.cross_list_from_beg()
print("\n")
print("Po usunieciu ostatniego elementu:\n")
fun.delete_last()
fun.cross_list_from_beg()
print("\n")
print("Po przejsciu listy od tyłu:\n")
fun.cross_list_from_end()
print("\n")
print("Najlepszy wynik kolokwium osiagnal student:")
fun.best_grade()
