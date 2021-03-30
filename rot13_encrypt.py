'''
Code from "Python One-Liners" by Christian Mayer
2020, no starch press
'''

# Data
abc = "abcdefghijklmnopqrstuvwxyz"
s = "thexcommiexrussiansxarexcoming"

# One-Liner
rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])

# Result
print(rt13(s))
print(rt13(rt13(s)))

