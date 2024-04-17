from pwn import *
from time import *

# This code is going to be used to find time intervals for this process.
# This can be found by checking two numbers, 00^(n-1) and 10^(n-1) where n is the length.
def findintervalcorrect(process):
    process.clean()
    start0 = time.time()
    process.sendline(b"0"*32)
    print (process.recvuntil("ERROR: Verification failed!"))
    end0 = time.time()
    process.clean()
    start1 = time.time()
    process.sendline(b"1"+b"0"*31)
    print (process.recvuntil("ERROR: Verification failed!"))
    end1 = time.time()
    return abs((end0 - start0) - (end1 - start1))
    

# Starting StrangeSystem
beginCommand = '/home/reverbfortuna/Documents/cpts327 hw3/StrangeSystem'
proc = process(beginCommand)

# Logging in
proc.sendline(b"11758263")
print (proc.recvuntil("Enter your 32-bits PIN code (in binary form like PIN in pincode.log):"))

# Work goes here
interval = findintervalcorrect(proc)

# Exiting
proc.close()

print("\nInterval of " + str(interval) + " seconds.\n")
