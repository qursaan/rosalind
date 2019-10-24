# Given: Two positive integers a and b (a < b < 10000).
#
# Return: The sum of all odd integers from a through b, inclusively.
#
# Hint: You can use a % 2 == 1 to test if a is odd.

def sum_all_odd(a, b):
    sum = 0
    if a%2==0: a+=1
    for i in range(a, b+1, 2):
        sum +=i
    return sum


print(sum_all_odd(7134,7500))
# 1339011

print(sum_all_odd(100,200))
# 7500

print(sum_all_odd(4383,9146))
# 16111848
