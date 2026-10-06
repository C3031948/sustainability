from random import random
counter = 0
for j in range(10**6):
    heads = 0
    for i in range(10):
#       print(random())
        if random() < 0.5:
            heads += 1
#           print("H")
#       else:
#           print("T")
#       if heads >= 7:
#           print("yes")
 #  print(heads)
    if heads >= 7:
        counter += 1
print(counter)
print(counter/10**6)
 
