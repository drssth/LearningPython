#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# int, float, string, list, dict
a,b,c,d,e = 17,17.5,"doesn't",[1,2,3],{"key":'value'}
print(a,b,c,d,e)


# class
class Person(object):
    NAME = 'Person'
    ATTRIBUTES = ['gender', 'age', 'weight', 'height']
    
    def __init__(self, name):
        self.name = name
        
    def __call__(self):
        return self.name
        
    def __lt__(self, other):
        return self.name < other.name
    def __le__(self, other):
        return self.name <= other.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return self.name != other.name
    def __gt__(self, other):
        return self.name > other.name
    def __ge__(self, other):
        return self.name >= other.name
        
    def __str__(self):
        return '<Person(name={})>'.format(self.name)
        
    def __enter__(self):
        print('enter object {}'.format(Person.NAME))
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit object {} {}'.format(Person.NAME, self.name))
        del self.name
        
    def __del__(self):
        print('delete object')
        
        
        
p1 = Person('Doris')        
p2 = Person('Mike')
print(p1,p2, p1>p2)
print(p1.NAME, p1.NAME, Person.NAME)

with Person("David") as p:
    print(p, p.name)
    
    
# list functions
l = list(range(1,11))
print(l)
ll = []
for i,v in enumerate(l):
    ll.append((i,v))
print(l[3:-1])
print(ll)
l.sort(reverse=True)
print(l)
ll.sort(key=lambda x:x[1], reverse=True)
print(ll)
llr = sorted(ll, key=lambda x: x[1], reverse=True)
print(llr)

e = (5,6)
print(llr.index(e))
llr.remove(e)
print(llr)
#print(llr.index(e))