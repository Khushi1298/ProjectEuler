sum = 0
i= 1
count = 0 
while(i>=1) : 
       print("i : ",i)
       sum=int((i+1)*(i/2))
       print("sum:",sum)
       print("Factors of",sum,":")
       count = 0
       for j in range(1, int(sum**0.5) +1):
            if sum % j== 0 :
                #print(j)
                count+= 1 
       if (count*2 > 500) : 
                     break
       i+= 1