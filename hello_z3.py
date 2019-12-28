#!/usr/bin/env python
from z3 import *
from pwn import *

r = remote('127.0.0.1', 9003)

for j in range(0,100):
    s = Solver()
    x = Int('x')
    y = Int('y')
    for i in range(0,2):
        line = r.recvline().strip()
        print line
        lrhs = line.split('=')        
        ### fast way to exchange parameter
        ### and execute the instruction
        exec("s.add(%s==%s)"%(lrhs[0], lrhs[1]))
        ### 
    # assert s.check() == sat
    if(s.check() == sat):
        print(s.model()[x])
        r.sendlineafter('x = ', str(s.model()[x]))
        r.sendlineafter('y = ', str(s.model()[y]))
            
r.interactive()
