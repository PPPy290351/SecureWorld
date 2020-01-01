#!/usr/bin/env python

from z3 import *

key = [21, 23, 9, 22, 3, 16, 17, 7, 8, 10, 11, 4, 0, 2, 13, 6, 1, 14, 18, 19, 5, 20, 12, 15]
check_values = [247, 220, 217, 225, 154, 146, 217, 173, 173, 244, 245, 225, 199, 148, 106, 163, 159, 106, 106, 173, 244, 244, 173]

a = Int('a')
b = Int('b')
c = Int('c')
d = Int('d')
e = Int('e')
f = Int('f')
g = Int('g')
h = Int('h')
i = Int('i')
j = Int('j')
k = Int('k')
l = Int('l')
m = Int('m')
n = Int('n')
o = Int('o')
p = Int('p')
q = Int('q')
r = Int('r')
s = Int('s')
t = Int('t')
u = Int('u')
v = Int('v')
w = Int('w')
x = Int('x')
arr = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x]
sol = Solver()
sol.add(arr[0] == 102)
sol.add(arr[1] == 108)
sol.add(arr[2] == 97)
sol.add(arr[3] == 103)
for k1, k2 in zip(key[:-1], key[1:]):
    print('the value: ' + str(check_values[0]))
    sol.add(arr[k1] + arr[k2] == check_values[0])
    check_values = check_values[1:]

if sol.check() == sat:
    print(sol.model())
    m = sol.model()
    print (sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0])))
else:
    print("No")
