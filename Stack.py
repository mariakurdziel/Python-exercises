#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:48:02 2017

@author: maria
"""

class Node:
    
    def __init__(self,znak):
        self.znak=znak
        self.next=None
        
    def __str__(self):
        return str(self.znak)
        
class Filo:
    def __init__(self):
        self.head=None
        self.counter=0

    def push(self,znak):
        new=Node(znak)
        if not self.head:
            self.head=new
        else:
            new.next=self.head
            self.head=new
        self.counter+=1
            
    def pop(self):
       
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
       
        
        
    def isempty(self):
        if self.counter==0:
            print("Stos pusty!!")
            
    def prints(self):
        wsk=self.head
        while wsk:
            print(wsk)
            wsk=wsk.next
            
filo=Filo()            
            
filo.push(1)
filo.push(2)
filo.push(3)
filo.push(4)
filo.push(5)
filo.prints()
filo.pop()
filo.pop()
filo.pop()
filo.pop()
filo.pop()
filo.isempty()
