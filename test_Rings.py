from exorings3.exorings3 import *

# generate a Ring object p

radius = np.arange(10)
tau = (1. -  np.power(np.arange(10)/20,0.3))*3.

p = Ring(radius, tau)

#p = Ring()

# add a segment
p.addRing([2.5,0.8])

# delete a segment
p.delRing(4.2)

import matplotlib.pyplot as plt

print(p.segments)

plt.scatter(p.getRadius(),p.getTau())
(r,t) = p.showRing()
plt.step(r,t, where='pre', zorder=-10)
plt.xlim(0,20)
plt.ylim(3,-0.1)
plt.xlabel('Radius')
plt.ylabel('Optical Depth')
plt.title('Ring system')

plt.show()
