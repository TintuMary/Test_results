import pandas as pd 
import numpy as np 

def collatz_sequence(n, map_n): 
      
    # If value already  
    # computed, return it 
    if n in map_n: 
        return map_n[n] 

    if(n == 1): 
        map_n[n] = 1
  
    # Even case 
    elif(n % 2 == 0): 
        map_n[n] = 1 + collatz_sequence(n//2, map_n) 
  
    # Odd case 
    else: 
        map_n[n] = 1 + collatz_sequence(3 * n + 1, map_n) 
      
    return map_n[n] 
  
def sequence(n): 
      
    # empty Map store seq lengths 
    map_n = {} 
      
    collatz_sequence(n, map_n) 
  
    num, l =-1, 0
      
    for i in range(1, n): 
          
        # calculate and store value 
        if i not in map_n: 
            collatz_sequence(i, map_n) 
          
        slen = map_n[i] 
        if l < slen: 
            l = slen 
            num = i
             
    return (num, l) 
  
print(sequence(1000000)) 