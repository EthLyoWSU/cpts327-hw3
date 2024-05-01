# Given information
p2ga = 55
p2gb = 261
q = 509
P = 1019
g = 3

set_dictionary = {}

# Code generates entire possible G
for i in range(0, P):
    set_dictionary[i] = pow(g, i, P)

print(str(set_dictionary))