from itertools import combinations

# inputNum = int(input())
# listofposs = [36.]
# listforposscalc = [[] for i in range(20)]
#
# for i in range(36):
#     listforposscalc[0].append(1)
#
# for i in range(1, 20):
#     total = 0
#     temp = []
#     for j in range(1, 37):
#         total += sum(listforposscalc[i-1][j:])
#         temp.append(sum(listforposscalc[i-1][j:]))
#     listforposscalc[i] = temp
#     listofposs.append(total)
#
#
# def get_ans(inputNum):
#     i = 0
#     while inputNum > 0:
#         inputNum -= listofposs[i]
#         i += 1
#     i -= 1
#     inputNum += listofposs[i]
#     ans = []
#     for place in range(i):
#         value = ans[-1] if len(ans) > 0 else 0
#         for k in range(value, 36):
#             if len(ans) > 0:
#                 try:
#                     inputNum -= listforposscalc[i-place][:][k+1]
#                 except IndexError:
#                     pass
#             else:
#                 inputNum -= listforposscalc[i - place][k]
#             if inputNum < 1:
#                 if len(ans) > 0:
#                     inputNum += listforposscalc[i - place][:][k]
#                     ans.append(k + 1)
#                 else:
#                     inputNum += listforposscalc[i - place][k]
#                     ans.append(k)
#                 break
#     if len(ans) > 0:
#         ans.append(inputNum+ans[-1])
#     else:
#         ans.append(inputNum-1)
#     for i, thing in enumerate(ans):
#         if thing < 26:
#             ans[i] = chr(int(65+thing))
#         else:
#             ans[i] = thing - 26
#     return ans
#
#
# print([(get_ans(x), x) for x in range(8000)])

while False:
    pass

# SOLUTION

# inputNum = int(input())
# i = 0
# nums = []
# while len(nums) < inputNum:
#     i += 1
#     for j in combinations('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', i):
#         nums.append(j)
#     print(i, len(nums))
# print(nums[inputNum-1])

while False:
    pass

# SOLUTION

from math import comb

print(comb(35, 2))
n = int(input())

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def build(n, targetLen, ans=""):
    if targetLen == 0:
        return ans
    start = (alpha.index(ans[-1]) + 1) if ans else 0
    for letter in range(start, 36):

        can = comb(36 - (letter + 1), targetLen - 1)

        if can >= n:
            return build(n, targetLen - 1, ans + alpha[letter])
        n -= can


targLen = 1
while comb(36, targLen) < n:
    n -= comb(36, targLen)
    targLen += 1

print(build(n, targLen))

while False:
    pass

# SOLUTION

# def a():
#     from math import comb
#     # comb is basically the choose function
#
#     n = int(input())
#     # Numbers come after letters in the alphabet here
#     # Looked at solution because I was not doing well
#
#     # Basically I needed to know that the choose function would be useful and the knowledge of the comb function in math
#
#     # This stores the alphabet and numbers in the right order
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#
#     def process(n,length,current = ""):
#         # This is the terminating condition in our recursion
#         if length == 0:
#             return current
#         # This gets the index of the first character that could be added to the string
#         start = alpha.index(current[-1])+1 if current else 0
#         # This tests all of the combos with each of the indexes
#         for i in range(start,36):
#             # combos is how many combos there are after this one, the options after
#             combos = comb(36 - i - 1, length-1)
#             # If this condition is satisfied then this value of i is the right character
#             if combos >= n:
#                 return process(n,length-1, current + alpha[i])
#             # Otherwise just reduce n by the combos, as we are discarding the other combos
#             n -= combos
#
#     # This little loop figures out the how many characters long the password is going to be using comb
#     length = 1
#     while comb(36,length) < n:
#         n -= comb(36,length)
#         length += 1
#
#     # We then process the password with what we know is the right length
#     print(process(n, 36))
#
# a()

while False:
    pass

# SOLUTION

# """
# 2014: Q3 "Increasing passwords"
#
# This is a classic Q3 combinatorics question, with some dynamic programming
# thrown in. The key is to find the recurrence relation, and calculate it in a
# fast enough way.
#
# Hopefully it's not a huge leap to spot that a valid password beginning with A of
# length N can be A followed by either [all of the passwords of length (N - 1)
# beginning with B, all of the passwords of length (N - 2) beginning with C, ...].
#
# You can write this out as a table
#
# +------+-------+-------------+-----+
# |      |   1   |     2       | ... |
# +------+-------+-------------+-----+
# | A    |   1   | B+C+D+E+... |     |
# | B    |   2   | C+D+E+...   |     |
# | etc. |       |             |     |
# +------+-------+-------------+-----+
#
# This 2D grid should scream dynamic programming to you, but tbh I think in this case
# in a language like Python, it seems way easier to just memoise the results using a
# dictionary.
# """
#
#
# def count(begins_with, length, memos):
#     assert length <= 36 and length > 0
#     assert begins_with >= 0 and begins_with < 36
#
#     if length == 0:
#         return 0
#     if length == 1:
#         return 1
#
#     if (begins_with, length) in memos:
#         return memos[begins_with, length]
#
#     result = sum(count(i, length - 1, memos) for i in range(begins_with + 1, 36))
#
#     memos[begins_with, length] = result
#     return result
#
#
# translate_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# assert len(translate_char) == 36
#
#
# def count_char(char, length):
#     return count(translate_char.find(char), length, {})
#
#
# def compute_length_of_nth_password_and_number_of_shorter_passwords(nth, memos):
#     cumulative = 0
#     shorter_passwords = 0
#
#     for length_candidate in range(1, 37):
#         for c in range(36):
#             this_count = count(c, length_candidate, memos)
#             cumulative += this_count
#
#             if cumulative >= nth:
#                 return length_candidate, shorter_passwords
#
#         shorter_passwords = cumulative
#
#     raise RuntimeError("n is too large.")
#
#
# def solve(nth):
#     result = []
#     memos = {}
#
#     # Start by figuring out what the length should be, and how many passwords
#     # we're skipping over due to length.
#     (
#         length,
#         shorter_passwords,
#     ) = compute_length_of_nth_password_and_number_of_shorter_passwords(nth, memos)
#     nth -= shorter_passwords
#
#     # Then compute each character individually.
#     previous_character = -1
#
#     while length > 0:
#         cumulative = 0
#
#         for c in range(previous_character + 1, 36):
#             cumulative += count(c, length, memos)
#
#             if cumulative >= nth:
#                 result.append(translate_char[c])
#                 previous_character = c
#                 break
#
#         nth = nth - (cumulative - count(previous_character, length, memos))
#         length -= 1
#
#     return "".join(result)
#
#
# if __name__ == "__main__":
#     nth = int(input())
#     print(solve(nth))

while False:
    pass

# SOLUTION

# from functools import lru_cache
# from math import comb
#
# alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
#
# def password(n, word, length):
#     if length <= 0:
#         return word
#     if len(word) == 0:
#         a = 0
#     else:
#         a = alpha.index(word[-1]) + 1
#
#     for letter in range(a, len(alpha)):
#         perms = comb(36 - letter - 1, length-1)
# #        print(letter, perms, n, length)
#         if n <= perms:
#             return password(n, word + alpha[letter], length-1)
#         n = n - perms
#
# def getLength(n):
#     l = 1
# #    print(getLen(36, l))
# #    while n > getLen(36, l):
#     while n > comb(36, l):
#         n -= comb(36, l)
#         l += 1
#     return l,n
#
# n = int(input())
#
# l,n = getLength(n)
# print(password(n, "", l))
#
# """
# b) 14, BIO, NTU, BIO14, ABCDE
#
# c) 68719476734
# passwords up to length of 36 will be accepted
#
# d) There is only 1 pair that fulfills this criteria: ATUVWXYZ0123456789 and BCDEFGHIJKLMNOPQRS. Given a password,
# the next password will either have the same number of digits or 1 more digit. For the number of digits between the
# passwords to be 36, without repeats, both passwords must contain 18 digits. As the passwords are ordered, the first
# password must contain the A. As the second password cannot contain an A, the first password must be the last password
# beginning with A.
#
# """
#
# def c():
#     ans = 0
#     for length in range(1,36):
#         ans += comb(36, length)
#     print(ans)
