# https://www.codewars.com/kata/582dafb611d576b745000b74/train/python
def method1(fighter):

    if(fighter.lower() == 'george saint pierre'):
        return("I am not impressed by your performance.")
    elif(fighter.lower() == 'conor mcgregor'):
        return("I'd like to take this chance to apologize.. To absolutely NOBODY!")

statements = {
    'george saint pierre': "I am not impressed by your performance.",
    'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"
}

def method2(fighter):
    return statements[fighter.lower()]

val1 = method1('George Saint Pierre')
val2 = method2('Conor McGregor')

print(val3)
