#Program to write the multiplication table of a number

num=int(input("Enter the number :"))    #Take user input
mul=int(input("Enter how many multiplies required : "))     #Take user input
for n in range(1,mul+1):   #loops from 1 to number of multiplies mentioned by user
    product=num * n     #calculating the product
    print(f"{num}x{n}={product}")   #Display results