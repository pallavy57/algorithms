constant < log log pow(n) < log pow(n) < n pow(1/3) < n pow(1/2) < n < n pow(2) < n pow(3) < n pow(4) < 2 pow(n) < n pow(n)
O notation
Ignore the lower oredr terms, constant
HIghest order term  - O(n2)

for upper bound = O notation
For constants = O(1)
For n as high order like n/4, 2n + 3, n/100 + logn = O(n)
For n pow 2 + b , 2 n pow 2 = O(n pow 2)



for lower bound = Omega notation

for exact bound = theta notation both high and low

n <= 2n + 3 <= 3n
n>=0      n<=3

In a loop, how to find how many times a loop will run
if n is the input of list
c is some constant with which we are incrementing the loop
numof times loop will run is n/c times
@(n)

????????????????????????????????????????
i = 1
or i = n
while(i<n>):
i = i *c  or i = i//c

number of iterations;@(logn)
number of iterations;@(logn)

???????????????????????????????????????????
i=2
while(i<n>):
i = i**c  or i = i//c

number of iterations; @(log c log n) 

???????????????????????????????????????????

In nested loop:
 @n * @logn

n=5
m=4
#FirstExampleLoop
i=0
while i<n:
    i=i+c
    
#SecondExampleLoop
i=n
while i>0:
    i=i-c
    
#ThirdExampleLoop
i=1
while i<n:
    i=i*c
    
#FourthExampleLoop
i=n
while i>1:
    i=i/c
    
#FifthExampleLoop
i=2
while i<n:
    i=i**c
    
#SubsequentLoops
i=0
while i<n:
    i=i+2
    
i=1
while i<n:
    i=i*3
    
i=1
while i<100:
    i=i+1
    
#NestedLoop
i=0
while i<n:
    j=1
    while j<n:
        j=j*2
    i=i+1
    
#MixedLoop
i=0
while i<n:
    j=1
    while j<n:
        j=j*2
    i=i+1
i=0
while i<n:
    j=1
    while j<n:
        j=j+1
    i=i+1
    
#MultipleInput
i=0
while i<n:
    j=1
    while j<n:
        j=j*2
    i=i+1
i=0
while i<m:
    j=1
    while j<m:
        j=j+1
    i=i+1

def fun(n):
    if n==1:
        return
    for i in range(n):
        print("GFG")
    fun(n/2)
    fun(n/2)
https://www.youtube.com/watch?v=6zhGS79oQ4k
