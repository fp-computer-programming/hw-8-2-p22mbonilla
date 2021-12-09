# Author MB 12/09/2021

def even_sum(lst):
    total = 0
    for x in lst:
        if x % 2 != 0:
            break
        else:
            total += x
            x += 1
    return total

print(even_sum([2, 4, 6, 8, 9]) == 20)
print(even_sum([13, 12, 10]) == 0)
print(even_sum([14, 16, 32]) == 62)
