#Program to find vowels and consonants in a sentense
#Using manual menthod
data=input("Enter the sentence : ")     #Take user input
vowelcount=0
consonantcount=0
data1=data.lower()  #Converting data to lowercase
for n in data1:
    if n.isalpha(): #Checking if character is alphabet
        if (n=='a' or n=='e' or n=='i' or n=='o' or n=='u'): #we can also use -> if n in 'aeiou'
            vowelcount=vowelcount+1
        else:
            consonantcount=consonantcount+1

print(f"Number of vowels in a sentence is {vowelcount}")    #Display results
print(f"Number of consonants in a sentence is {consonantcount}")

#using functions

# def count_vowels_consonants(sentence):
#     vowels = 0
#     consonants = 0
#
#     for ch in sentence.lower():
#         if ch.isalpha():
#             if ch in 'aeiou':
#                 vowels += 1
#             else:
#                 consonants += 1
#
#     return vowels, consonants
#
# data = input("Enter a sentence: ")
# v, c = count_vowels_consonants(data)
#
# print(f"Vowels: {v}")
# print(f"Consonants: {c}")

#using list comprehensions-using [] /generator expressions- using ()

# data = input("Enter a sentence: ").lower()
#
# vowels = sum(1 for ch in data if ch in 'aeiou')
# consonants = sum(1 for ch in data if ch.isalpha() and ch not in 'aeiou')
#
# print(f"Vowels: {vowels}")
# print(f"Consonants: {consonants}")