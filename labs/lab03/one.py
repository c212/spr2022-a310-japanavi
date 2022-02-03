# 1. Prove that for a and b unknown truth values we have
# not (a and b) == (not a) or (not b)

a = True
b = False

print(not (a and b) == (not a) or (not b))


# Simplify, for a and b unknown truth values
# not ((not a) or (not b))

# not ( not( not (a))) == not (a)
