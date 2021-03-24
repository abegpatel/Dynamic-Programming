# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:57:30 2021

@author: Abeg
"""
"""
def fibonacci(n):  
      
    # Taking 1st two fibonacci nubers as 0 and 1  
    f = [0, 1]  
      
      
    for i in range(2, n+1): 
        f.append(f[i-1] + f[i-2]) 
    return f[n] 
print(fibonacci(10)) 
"""
#fibonancci using dynamic programming
def fib(n):
  if(n<2):
    return n
  return fib(n-1)+fib(n-2)
cache={}
def fun(n):
  if(n in cache):
    return cache[n]
  else:
    if(n<2):
      return n
    else:
      cache[n]=fib(n-1)+fib(n-2)
    return cache[n]
print(fun(10))
