# Given information
p2ga = 55
p2gb = 261
q = 509
P = 1019
g = 3

setList = []

def returniList(gIn, G):
    matchingList = []
    for i in range(0, P):
        if G[i] == gIn:
            matchingList.append(i)
    print(str(matchingList))
    return matchingList

# Code generates entire possible G
for i in range(0, P):
    setList.append( pow(g, i, P))

print(str(setList))

# Now that we have the list of G, we can narrow down to two lists.
# These lists will contain all of the i for which gi = ga or gb.
print("Finding Matching list for ga")
gamatch = returniList(p2ga, setList)
print("Finding Matching list for gb")
gamatch = returniList(p2gb, setList)