#Program to write fibonacci series
n = int(input("Enter the number of terms: ")) #Take user input
a, b = 0, 1 #Initialize frst 2 numbers

if n >= 1:  #Check the conditions eg :when n=0/1 its required
    print(a, end=' ')
if n >= 2:
    print(b, end=' ')

for i in range(n-2):    #Loop starts from 2 as already frst 2 numbers are fixed
    c = a + b
    print(c, end=' ')
    a, b = b, c  # update previous two numbers

#using lists
# n=int(input("Enter the number of terms : "))
# fib=[0,1]
# for i in range(2,n):
#     fib.append(fib[i-1]+fib[i-2])
#
# print(*fib[:n])


