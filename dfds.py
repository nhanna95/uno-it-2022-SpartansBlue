import math 

i = 41
while True: 
    if ((40 + i + math.sqrt(40 * i)) / 3) == math.floor(((40 + i + math.sqrt(40 * i)) / 3)):
        print(i)
        break
    else:
        i += 1