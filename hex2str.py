#!/usr/bin/env python3

shellcode = [
 '0x7d212121',
 '0x476e6952',
 '0x74535f63',
 '0x3147346d',
 '0x5f446e6c',
 '0x465f5530',
 '0x597b4654',
 '0x43747372',
 '0x6946794d'
]

for i in range(len(shellcode)-1,-1,-1): # end : -1
    for j in range(len(shellcode[i])-1,2,-2):
        c = '0x' + shellcode[i][j-1] + shellcode[i][j]
        d = chr(int(c,16))
        print(d,end='')
