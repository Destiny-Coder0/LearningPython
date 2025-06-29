# 1- Write a function that displays a given word on the screen for a specified number of times.

""" 
def repeater(word,times):
    print(word * times)

word=input("Enter a word to repeat: ")
times = int(input("Enter the number of times you want to repeat: "))

repeater(word, times)
 """

# 2- Write a function that converts an unlimited number of parameters sent to itself into a list.

""" 
def convertToList(*args):
    list= []
    for arg in args:
        list.append(arg)

    return list

result = convertToList(1,2,3,4,5,6,7,8,9,10, "New York", "London")

print(result) 
"""

# 3- Return the exact divisors of a number sent to itself as a list.

""" 
def findTheDivisors (num):
    divisors = []

    for i in range (2, num):
        if num%i==0:
            divisors.append(i)

    return divisors

print(findTheDivisors(20)) 
"""
