# imoort math  for power 
import math 
ans = 0 
for i in range (2,200000) :
    sum = 0
    t = i
    while i> 0 : 
       r = i%10 
       p = math.pow(r,5)
       sum = sum+p 
       i = i// 10 
    if t== sum :
               print(t)
               ans = ans + sum 
print("sum is ",ans)
        
     
