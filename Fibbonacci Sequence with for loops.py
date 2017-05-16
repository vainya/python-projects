import random 

out = [0, 1]

for n in range(40):
    result = out[-1] + out[-2]
    out.append(result)

print out[-1]

