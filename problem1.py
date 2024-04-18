from pwn import *
from time import *

# This code checks a particular bit input. If it is not correct, it returns the time it took, otherwise -1
def sendtostrangebitcheck(input, process):
    temp = 0
    process.clean()
    start = time()
    process.sendline(input)
    output = process.recvline_startswith("[***]", False, timeout=60)
    print((output))
    end = time()
    if "ERROR" in str(output):
        process.clean()
        process.sendline(b"YES")
        print("\n" + str(end - start) + "\n")
        return end - start
    else:
        return -1

# This code is going to be used to find time intervals for this process.
# This can be found by checking two numbers, 00^(n-1) and 10^(n-1) where n is the length.
def findintervalcorrect(process):
    process.clean()
    time0 = sendtostrangebitcheck(b"0"+b"0"*31, process)
    time1 = sendtostrangebitcheck(b"1"+b"0"*31, process)
    # The difference between the time it takes to calculate each two is the time difference between
    # a correct bit and an incorrect bit.
    return abs(time0 - time1)

def findanswer(process, differencetime, currentknown, time):
    # We don't know how long wrong or right takes. But we know that wrong is always faster.
    # If this is the first time through, then we need to establish a time.
    if (time == 0):
        print("\nBeginning\n")
        # Then we need to check both and determine which is longer.
        time0 = sendtostrangebitcheck(b"0"+b"0"*31, process)
        time1 = sendtostrangebitcheck(b"1"+b"0"*31, process)
        if time0 > time1:
            return findanswer(process, differencetime, b"0", time0)
        else:
            return findanswer(process, differencetime, b"1", time1)
    else:
        if (len(currentknown) == 32):
            newtime = sendtostrangebitcheck(currentknown, process)
            return currentknown
        # Create our input to test the timing of.
        print("\n"+ str(currentknown) + str(b"0"*(31-len(currentknown))) +"\n")
        # Test the timing
        newtime = sendtostrangebitcheck(currentknown+b"1"+b"0"*(31-len(currentknown)), process)
        oldtimehigh = time + 0.15
        if (newtime != -1):    
            if (newtime > oldtimehigh):
                return findanswer(process, differencetime, currentknown+b"1", newtime)
            else:
                return findanswer(process, differencetime, currentknown+b"0", time)
        else:
            return currentknown

# Starting StrangeSystem
beginCommand = '/home/reverbfortuna/Documents/cpts327 hw3/StrangeSystem'
proc = process(beginCommand)

# Logging in
proc.sendline(b"11758263")
proc.recvuntil("Enter your 32-bits PIN code (in binary form like PIN in pincode.log):")

# Work goes here
#interval = findintervalcorrect(proc)
output = findanswer(proc, 0, b"", 0)
print("\n\n" + str(output) + "\n\n")


proc.interactive()

# Exiting
print(proc.recvall(timeout = 1))
proc.close()


