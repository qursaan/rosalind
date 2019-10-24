# Given: A string of length at most 10000 letters.
#
# Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.
# Sample Dataset: We tried list and we tried dicts also we tried Zen
# Sample Output: and 1 We 1 tried 3 dicts 1 list 1 we 2 also 1 Zen 1
#
# Hints:
#
# To iterate over words in string you can split it by space:
# for word in str.split(' '): print(word)
# To have nice output of dictionary you can use .items() method:
# for key, value in dict.items(): print(key) print(value)

def count_occurance(stringval):
    dlist = {}
    for word in stringval.split(' '):
        if word in dlist:
            dlist[word] += 1
        else:
            dlist[word] = 1
    for (k, v) in dlist.items():
        print(k, v)


count_occurance('When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be')

# When 1
# I 2
# find 1
# myself 1
# in 4
# times 1
# of 11
# trouble 1
# Mother 2
# Mary 2
# comes 2
# to 3
# me 4
# Speaking 3
# words 7
# wisdom 7
# let 30
# it 36
# be 41
# And 3
# my 1
# hour 1
# darkness 1
# she 1
# is 4
# standing 1
# right 1
# front 1
# Let 6
# Whisper 4
# when 2
# the 4
# broken 1
# hearted 1
# people 1
# living 1
# world 1
# agree 1
# There 4
# will 5
# an 4
# answer 4
# For 1
# though 1
# they 2
# may 1
# parted 1
# there 2
# still 2
# a 2
# chance 1
# that 2
# see 1
# night 1
# cloudy 1
# light 1
# shines 1
# on 1
# Shine 1
# until 1
# tomorrow 1
# wake 1
# up 1
# sound 1
# music 1
# yeah 2
