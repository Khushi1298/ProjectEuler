#25 PROJECT What is the index of the first t
a=0
b=1
n=0
sum = 0
c=0
print(b)
while(n>= 0):
     c= a+b
     a = b
     b=c
     sum=0
     print("series: \n",c)
     while(c>0):
          rev=c% 10
          c= c//10
          sum += 1
     if (sum==1000):
             print("n:",n)
             break

     n+= 1

print("Term n:",n+2)