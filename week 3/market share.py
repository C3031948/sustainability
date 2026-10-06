import matplotlib.pyplot as plt
from random import random
times = []
Volture_owners = []
NeonDrive_owners = []
Volture = 0
NeonDrive = 0
for i in range(5):
    if random()<0.5:
        Volture += 1
    else:
        NeonDrive += 1
print(Volture, NeonDrive)
times.append(i)
Volture_owners.append(Volture)
NeonDrive_owners.append(NeonDrive)
for i in range(995):
    if random()<Volture/(Volture+NeonDrive):
        Volture += 1
    else:
        NeonDrive += 1
print(Volture, NeonDrive)
times.append(i)
Volture_owners.append(Volture)
NeonDrive_owners.append(NeonDrive)
plt.plot(times,Volture_owners)
plt.plot(times,NeonDrive_owners)
plt.xlabel('Time')
plt.ylabel('No. owners')
plt.legend(['Volture', 'NeonDrive'])
plt.show()