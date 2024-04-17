from pwn import *

# Starting StrangeSystem
beginCommand = '/home/reverbfortuna/Documents/cpts327 hw3/StrangeSystem'
proc = process(beginCommand)

# Logging in
proc.sendline(b"11758263")
print (proc.recvuntil("Enter your 32-bits PIN code (in binary form like PIN in pincode.log):"))

# Work goes here
proc.clean()
proc.sendline(b"0"*32)
proc.interactive()

print(proc.recvall(timeout = 1))

# Exiting
proc.close()
