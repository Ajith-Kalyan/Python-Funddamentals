#https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python
def array(string):
    string = string[2:-2]
    if len(string)==0:
        return None
    else:
        return string.replace(',',' ')

val = array(' 1 2 3 4 ')
print(val)