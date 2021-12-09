# Author MB 12/09/2021

def who_are_you(lst, what):
    total = 0
    for x in lst:
       if x == what:
           total += 1
    return total

print(who_are_you("cat", "t") == 1)
print(who_are_you("apple", "p") == 2)
print(who_are_you("supercalifragilisticexpialidocious", "i") == 7)
