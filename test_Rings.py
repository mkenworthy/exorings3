from exorings3.exorings3 import *
import matplotlib.pyplot as plt

# generate a Ring object p

radius = np.arange(10)
tau = (1. -  np.power(np.arange(10)/20,0.3))*3.

p = Ring(radius, tau)

#p = Ring()

print('Making a ring system with a power law')

plt.scatter(p.getRadius(),p.getTau())
(r,t) = p.showRing()
plt.step(r,t, where='pre', zorder=-6)
plt.xlim(0,20)
plt.ylim(3,-0.1)
plt.xlabel('Radius')
plt.ylabel('Optical Depth')
plt.title('Ring system')

# add a segment
p.addRing([2.5,0.8])
print('Added a ring at 2.5, 0.8')
plt.scatter(p.getRadius(),p.getTau())
(r,t) = p.showRing()
plt.step(r,t, where='pre', zorder=-8)

# delete a ring
p.delRing(4.2)
print('Added a ring at 2.5, 0.8')
plt.scatter(p.getRadius(),p.getTau())
(r,t) = p.showRing()
plt.step(r,t, where='pre', zorder=-10)

plt.show()

print(p.segments)
