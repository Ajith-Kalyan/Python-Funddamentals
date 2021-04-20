#https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
# Add the two digits and convert to binary string.
def add_binary(a,b):
    sum = a+b
    return bin(sum)

val = add_binary(1,1)
print("Value of 1st method = "+val)

#################################################
#              OR                  #

def add_bin(a,b):
    return("{0:b}".format(a+b))

value = add_bin(1,1)
print("Value of 2nd method = "+value)