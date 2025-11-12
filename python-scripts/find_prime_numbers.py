#Check if the entered number is prime or not
#note : prime numbers are only divisible by 1 and itself(0 and 1 are not prime)

num=int(input("Enter the number:")) # Take input from user
if num<=1: #checking if num is less than 1
    print(f"{num} is not a prime number")
else:
    prime_num=True #assuming entered num is prime
    for i in range(2,num):#checking our assumption
        num%i == 0 #if num is divided by any other number it will not be prime number
        prime_num=False
        break #once finding it is not prime no need to continue the loop so using break

    if prime_num: # using this condition to print the result
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")