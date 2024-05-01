# Given information
p2ga = 55
p2gb = 261
q = 509
P = 1019
g = 3

setList = []

# The following code takes a g value and G before returning an array of possible i values where gi = g
def returniList(gIn, G):
    matchingList = []
    for i in range(0, q):
        if G[i] == gIn:
            matchingList.append(i)
    print(str(matchingList))
    return matchingList

# Code generates entire possible G, index is i
for i in range(0, q):
    setList.append( pow(g, i, P))

print(str(setList))

# Now that we have the list of G, we can narrow down to two lists.
# These lists will contain all of the i for which gi = ga or gb.
print("Finding Matching list for ga")
gamatch = returniList(p2ga, setList)
print("Finding Matching list for gb")
gbmatch = returniList(p2gb, setList)

# Checking if (g^a)^b mod P and (g^b)^a mod P are the same. If they are we know a, b, and gab
for a in gamatch:
    for b in gbmatch:
        gabfromga = pow(pow(g, b), a, P)
        gabfromgb = pow(pow(g, a), b, P)
        if gabfromga == gabfromgb:
            print("Match found! gab = " + str(gabfromga) + " a = " + str(a) + " b = " + str(b))

# gab is 211, a is 106, and b is 356