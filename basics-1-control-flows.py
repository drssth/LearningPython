#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## if
x = 1
if x == 0:
    print('x==0')
elif x == 1:
    print('x==1')
else:
    print('x is {}'.format(x))
    
    
## for
l = list(range(1,20,2))
print(l)
ll = []
for i,v in enumerate(l.copy()):
    ll.append((i, v, v**2))
print(ll)



## while
a = 5
while a > 0:
    print('while', a)
    a -= 1