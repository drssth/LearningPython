#!/usr/bin/env python3
# -*- coding: utf-8 -*-



## function(inputs, *arguments, **keywords)
def test(input1, input2, *arguments, **keywords):
    print("positional-input", input1)
    print("positional-input", input2)
    print("-" * 40)
    for arg in arguments:
        print('positional or keyword arg', arg)
    print("-" * 40)
    for kw in keywords:
        print('keyword arg', kw, ":", keywords[kw])
        
        
test('test1', 'test2', 'command', 'cli', parg1='parg1', parg2='parg2')


## lambda function 
def increase(n):
    return lambda x : x + n
    
v = increase(3)
print(v)
print(v(1))
print(v(4))

n = v(3)
print(n)
n = v(3)
print(n)