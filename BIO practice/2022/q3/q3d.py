from math import *

ans = 0
fact = factorial(15)
for a in range(1,16):
    for b in range(1,a):
        ans += fact // (a*b)
output = ""
ans = str(ans)[::-1]
for i in range(0, len(ans), 3):
    output += ans[i:i+3] + ","
output = output[::-1][1:]
print(output)