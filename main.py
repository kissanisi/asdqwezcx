"""s = [1, 0]

for x in s:
    for y in s:
        for z in s:
            for w in s:
                if (w <= x) and ((y <= z) == (x <= y)):
                    print(x, y, z, w)

#x y z w
#0 1 1 0
#1 1 1 0
#0 0 1 0
"""
"""
for i in range(0, 256):
    b = bin(i)[2:].zfill(8)
    s = ''
    for j in b:
        s += '0' if j == '1' else '1'
    k = int(s,2)-i
    if k == 133:
        print(i)
"""

"""al = 'ABCDXYZ'
cnt = 0
for q in al:
    for w in al:
        for e in al:
            for r in al:
                qwer = q + w + e + r
                if q == 'X':
                    if qwer.count('X') == 1 and qwer.count('Z') == 0 and qwer.count('Y') == 0:
                        cnt += 1
                if q == 'Y':
                    if qwer.count('X') == 0 and qwer.count('Z') == 0 and qwer.count('Y') == 1:
                        cnt += 1
                if q == 'Z':
                    if qwer.count('X') == 0 and qwer.count('Z') == 1 and qwer.count('Y') == 0:
                        cnt += 1

print(cnt)"""

"""f = open('9')
s = []
for i in f.readlines():
    s.append(list(map(int, i.split())))
cnt = 0
for i in s:
    if i[0] * i[1] + i[1] * i[2] > i[0] * i[2] and i[1] * i[2] + i[0] * i[2] > i[0] * i[1] and\
            i[0] * i[1] + i[0] * i[2] >i[1] * i[2]:
        cnt+=1
print(cnt)"""

"""s = '9' * 1000

while '999' in s or '888' in s:
    if '888' in s:
        s = s.replace('888', '9', 1)
    else:
        s = s.replace('999', '8', 1)
print(s)
"""

"""cnt = 0
n = 49 ** 7 * 7 ** 20 - 7 ** 8 - 28
while n:
    if n%7 == 6:
        cnt+=1
    n//=7
print(cnt)"""
"""
for a in range(0,1000):
    if all((2*x+3*y<a) or (x>=y) or (y>24) for x in range(0,1000) for y in range(0,1000)):
        print(a)"""

"""def f(n):
    if n <= 1:
        return 0
    elif n > 1 and n % 2 == 0:
        return n // 2 + f(n - 1) + 2
    else:
        return f(n - 1) + 3 * n ** 2


print(f(49))"""

"""import fnmatch

for i in range(0,10**10,3147):
    if fnmatch.fnmatch(str(i),'1*4239?7'):
        print(i)"""

"""f = open('17 (1).txt')
s = []
mn = 10 ** 10
cnt = 0
for i in f.readlines():
    s.append(int(i))
mx = 0
for i in s:
    if str(i)[-1] == str(i)[-2]:
        mn = min(mn, i)

for i in range(len(s) - 1):
    if (str(s[i])[-1] == str(s[i + 1])[-2] or str(s[i])[-2] == str(s[i + 1])[-1]) and \
            (abs((s[i]) % 13 == 0 and abs(s[i + 1]) % 13 != 0) or (abs(s[i + 1]) % 13 == 0 and abs(s[i]) % 13 != 0)) and \
            s[i] ** 2 + s[i + 1] ** 2 <= mn ** 2:
        cnt += 1
        mx = max(mx, s[i] ** 2 + s[i + 1] ** 2)
print(cnt, mx)
"""
"""f = open('24 (1).txt').readline()
al = dict()
s = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for i in s:
    al |= {i:0}
for i in range(len(f) - 2):
    if f[i] == f[i + 1]:
        al[f[i + 2]] += 1
print(max(al.values()))
for i in al:
    if al[i] == 1547:
        print(i)"""

"""def f(s, e, pl, ym):
    if s > e:
        return 0
    elif s == e:
        return 1
    if pl:
        return f(s * 2, e, 0, 1) + f(s * 3, e, 0, 1)
    elif ym:
        return f(s + 1, e, 1, 0) + f(s + 2, e, 1, 0)
    else:
        return f(s * 2, e, 0, 1) + f(s * 3, e, 0, 1) + f(s + 1, e, 1, 0) + f(s + 2, e, 1, 0)


print(f(1, 22, 0, 0))
"""

"""f = open('26 (1).txt')
n = int(f.readline())
s = []
for i in f.readlines():
    s.append(list(map(int, i.split())))
s.sort(key=lambda x:x[1])
z = 0
cnt = 0
mx = 0
for i in s:
    if z <= i[0]:
        mx = max(i[0]-z,mx) if cnt != 0 else 0
        z = i[1]+15
        cnt += 1
s.sort()
print(mx)
print(cnt)"""


def mn3(n):
    k = n
    cnt = 0
    while k:
        if k % 3 == 0:
            cnt += 1
        else:
            return cnt if cnt < 8 else 8
        k //= 3


f = open('27-A (1).txt')
n = int(f.readline())
s = []
for i in f.readlines():
    s.append(int(i))
colvo3 = dict()
for i in range(0, 9):
    colvo3 |= {i: [0, 0, 0, 0]}
res = 0
for i in s:
    for j in range(8 - mn3(i), 9):
        res += colvo3[j][(4 - i % 4) % 4]

    colvo3[mn3(i)][i % 4] += 1
print(res)