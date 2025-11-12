entered_list = []     # Initialize an empty list to store user inputs
while True:           # Continuously take input from the user until 'done' is entered
    num = input("Enter the numbers in list - enter done to finish: ")
    if num.lower() == 'done':
        break
    entered_list.append(int(num))   # Add each number to the list

print(f"List you entered is {entered_list}")  # Display the list

largest = entered_list[0]   # Assume first number is the largest
smallest = entered_list[0]  # Assume first number is the smallest

for n in entered_list:      # Compare each number to find the largest and smallest
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(f"Largest num in the list is {largest} and smallest is {smallest}")  # Display results

#Finding largest and smalles number in the list using MAX and MIN functions

#largest=max(entered_list)
#smallest=min(entered_list)