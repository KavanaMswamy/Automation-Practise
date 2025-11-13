#Reversing using slicing function

data=input("Enter the string to be reversed: ") #Take user input
reversed_data=data[::-1]    #slice the string from end to start
print(f"Reversed string is {reversed_data}")    #Display results

#Reversing using reversed function

# data=input("Enter the string to be reversed: ")
# reversed_data=''.join(reversed(data))
# print(f"Reversed string is {reversed_data}")


# Reversing in manual way

# data=input("Enter the string to be reversed: ")
# num=0
# for i in data:
#     num=num+1
#
# print(f"Length of the string is {num}")
# temp=[]
# while num:
#     x=data[num-1]
#     temp.append(x)
#     num=num-1
# reversed_string = ''.join(temp)
# print(f"Reversed string is {reversed_string}")
