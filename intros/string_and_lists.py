# Problem
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
#
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
#
# Sample Dataset
# HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# 22 27 97 102
# Sample Output
# Humpty Dumpty

s = 'jaXee6cikwxJc1sVJFDOGfJ1RoUG98RecurvirostrafY4QFFgMtimurG78L2jJbqESahGgkMU3JqO6ayIfxvTCGEevK0Q05UBjgZMqPzN1MR77keZUlmy0qWcampestrisq5ssHa0ZehlsFHfd6VjhP4GBlmuOm9GnTKy4ljDG3w. 30 42 121 130'.split()
a = int(s[1])
b = int(s[2])+1
c = int(s[3])
d = int(s[4])+1

print(s[0][a:b] , s[0][c:d])
