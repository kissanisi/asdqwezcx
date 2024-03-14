"""s = '1'*99

while '111' in s:
    s = s.replace('111','22',1)
    s = s.replace('222','11',1)

print(s)"""
"""
from functools import lru_cache


@lru_cache

def f(n):
    if n == 0:
        return 0
    elif n%2==0:
        return f(n//2)
    else:
        return f(n-1)+1
cnt=0
for i in range(1_000_000_000):
    if f(i)==2:
        cnt+=1
print(cnt)"""

"""def sumin(n):
    k = 0
    for i in str(n):
        k += int(i)
    return k


for i in range(1000):
    k = sumin(i)
    dv = bin(i)[2:] + '0' if k % 2 == 0 else bin(i)[2:] + '1'
    i = int(dv, 2)
    k = sumin(i)
    dv = bin(i)[2:] + '0' if k % 2 == 0 else bin(i)[2:] + '1'
    i = int(dv, 2)
    k = sumin(i)
    dv = bin(i)[2:] + '0' if k % 2 == 0 else bin(i)[2:] + '1'
    i = int(dv, 2)
    if i > 2054:
        print(i)
"""
"""import turtle as t

m = 20
t.tracer(10)
t.speed(100)
t.left(90)
t.down()
for i in range(4):
    t.forward(8 * m)
    t.right(150)
    t.forward(8 * m)
    t.right(30)
t.up()
for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x * m, y * m)
        t.dot(2)
t.update()

input()"""

"""f = open('asf')
s = []
k = []
for i in f.readlines():
    s.append(list(map(int,i.split())))
    for j in list(map(int,i.split())):
        k.append(j)
cnt = 0
for i in s:
    for j in i:
        if i.count(j) == 1 and k.count(j) == 46:
            cnt+=1
print(cnt)"""

"""for A in range(1, 1000):
    if all(((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (A - x > y) for x in range(1, 1000) for y in
           range(1, 1000)):
        print(A)"""

"""n = 6 * 343 ** 5 + 5 * 49 ** 7 - 50

k = 0
while n:
    if n % 7 == 6:
        k += 1
    n //= 7
print(k)
"""

"""def f(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1

for i in range(2422000,2422080):
    if f(i):
        print(i)"""

"""def f(s, e):
    if s == e:
        return 1
    elif s > e:
        return 0
    else:
        return f(s + 1, e) + f(s * 3, e) + f(s + 2, e)


print(f(2, 9) * f(9, 11) * f(11, 12))
"""

"""f = open('17 (1).txt')
s = []
cnt, mx = 0, 0
for i in f.readlines():
    s.append(int(i))
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] * s[j] % 34 != 0:
            cnt += 1
            mx = max(s[i] + s[j], mx)

print(cnt,mx)"""

"""s = "ТИМОФЕЙ"
cnt = 0
for q in s:
    for w in s:
        for e in s:
            for r in s:
                for t in s:
                    k = q+w+e+r+t
                    if k.count("Т")>=1 and k.count("Й")<=1:
                        cnt+=1
print(cnt)"""

"""f = open('zadanie24_2.txt').readline()
cnt = 0
mx = 0
for i in f:
    if i == 'R':
        cnt += 1
        mx = max(mx, cnt)
    if i!='R':
        cnt=0
        
print(mx)
"""

"""f = open('26_6759.txt')
s = []
for i in f.readlines():
    s.append(int(i))
s.sort()
print(s)

print(sum(s[:6621]))
cnt = 0
for i in range(len(s)):
    if (i + 1) % 3 == 0:
        print(s[i], i)
    else:
        cnt += s[i]
print(cnt)
"""

"""f = open('27-B_2.txt')
s = []
for i in f.readlines():
    s.append(int(i))
mx14 = 0
for i in s:
    if i%14==0:
        mx14 = max(mx14,i)
mx = 0
for i in s:
    if mx < i and i != mx14:
        mx = i
print(mx14*mx)"""
"""
f = open('27-A (1).txt')
s = []

k = int(f.readline())
n = int(f.readline())

for i in f.readlines():
    s.append(int(i))

mx1 = [-10 ** 10, 1]
mx2 = [-10 ** 10, 1]
mx3 = [-10 ** 10, 1]
for i in range(len(s)):
    if mx1[0] < s[i]:
        mx1[0] = s[i]
        mx1[1] = i
for i in range(len(s)):
    if mx2[0] < s[i] and s[i] != mx1[0]:
        mx2[0] = s[i]
        mx2[1] = i
for i in range(len(s)):
    if mx3[0] < s[i] and s[i] != mx1[0] and s[i] != mx2[0]:
        mx3[0] = s[i]
        mx3[1] = i

print(mx1, mx2, mx3)
"""

s = [1, 0]
for x in s:
    for y in s:
        for w in s:
            for z in s:
                if (x or (not z)) and (x == (not w)) and (x <= y):
                    print(x, y, z, w)
