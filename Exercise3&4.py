#################################
####### Coding Exercise 3 #######
#################################
import string


def palindrome(line):
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.replace(' ', "")
    line = line.upper()
    for index in range(len(line)):
        if line[index] != line[-index -1]:
            return False
    return True

# 3.1
print("Hello World"[8])

# 3.2
print("Thinker"[2:5])
s ='hello'
print(s[1]) # output is 'e'
s = 'Sammy'

# 3.3
print(s[2]) # output is 'm'

# 3.4
print(set('Mississippi'))

# 3.5
print("Enter the number of phrases you would like to test as palindromes")
for i in range(int(input())):
    print("Enter the word or phrase you would like to test")
    print(palindrome(input()))

#################################
####### Coding Exercise 4 #######
#################################
# 4.1
list1 = [3, 'walrus', 2.0]
print(list1)

# 4.2
list2 = [1, 1, [1, 2]]
print(list2[2][1])

# 4.3
lst = ['a', 'b', 'c']
print(lst[1:]) # output is ['b', 'c']

# 4.4
weekdays = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}

# 4.5
D = {'k1': [1, 2, 3]}
print(D['k1'][1]) # output is 2

# 4.6
print(tuple([1, [2, 3]]))

# 4.7
print(set('Mississippi'))

# 4.8
print(set('Mississippi').union('X'))

# 4.9
print(set([1, 1, 2, 3])) # output {1, 2, 3}

# 4 Question 1
for num in range(2000, 3201):
    if num % 7 == 0:
        if num % 5 == 0:
            continue
        print(num, end = ", " )
print()

# 4 Question 2
print("Enter the number you would like the factorial of")
num = int(input())
product = 1
if num == 0:
    print(0)
elif num > 0:
    for index in range(1, num+1):
        product *= index
elif num < 0:
    for index in range(num, 0):
        product *= index
print(product)

# 4 Question 3
print("Enter the number you would like to use to generate the dictionary")
num = int(input())
dict = {}
for index in range(num):
    dict[index] = index**2
print(dict)

# 4 Question 4
print('provide comma seperated list of numbers')
line = input()
line = line.split(',') # line is now a list of strings
lst = []
for item in line:
    lst.append(int(line[item]))
tup = tuple(lst)
print(lst)
print(tup)

# 4 Question 5


class ExObject:

    def __init__ (self):
        self.text = 'I am the walrus'

    def getString (self):
        return self.text

    def printString (self):
        print(self.text)

