#tips - https://youtu.be/WEP3DVTjKCc?list=PLi0EGg6K7IY36J9T9ZP00VOKV5P1VVpD0

#Multiple input :

'''
x,y = input("input two numbers: ").split()
print("first number :"+x)
print("second number :"+y)
'''


#swap numbers
'''
a,b = 3,4
a,b=b,a
print(a)
print(b)
'''

#remove duplicate from a list
# a as list
a = [1,2,5,3,66,55,2,4,2,3,1,5,1,5,1,2,2,4,3,9,2,4]

#to remove duplicate we convert list to set and agian convert set to list below
'''
b = list(set(a))
b.sort()
print(b)
'''

#to find maximum repeated number in the list
'''
repeated = max(set(a),key= a.count)
print(repeated)
'''

#find square of only odd numbers
#method 1
'''
odd_square = []
for i in range(11): #to get odd numbers within 11
    if i%2 == 1:
        odd_square.append(i**2)

print(odd_square)
'''

#method 2
'''
odd_square = [i**2 for i in range(11) if i%2 ==1]
print(odd_square)
'''

#pass any number of argument to a function use *

def add(*a):
    result = 0
    for i in a:
        result = result + i
    return result

val = add(1,2,3) #you can pass any number of argument
print(val)
 
