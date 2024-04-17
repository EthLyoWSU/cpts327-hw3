from pwn import *
from time import *

# This code checks a particular bit input. If it is not correct, it returns the time it took, otherwise -1
def sendtostrangebitcheck(input, process):
    process.clean()
    start = time()
    process.sendline(input)
    output = process.recvuntil("ERROR: Verification failed!", False, timeout=60)
    process.clean()
    process.sendline(b"YES")
    end = time()
    if output == '':
        return -1
    else:
        return end - start

# This code is going to be used to find time intervals for this process.
# This can be found by checking two numbers, 00^(n-1) and 10^(n-1) where n is the length.
def findintervalcorrect(process):
    process.clean()
    time0 = sendtostrangebitcheck(b"0"+b"0"*31, process)
    time1 = sendtostrangebitcheck(b"1"+b"0"*31, process)
    # The difference between the time it takes to calculate each two is the time difference between
    # a correct bit and an incorrect bit.
    return abs(time0 - time1)
    

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
