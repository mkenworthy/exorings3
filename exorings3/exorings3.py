'''
exorings3 - an updated version of the exorings code with object abstraction and updated for Python 3
'''
from astropy.table import Table
import numpy as np

class Ring(object):
    '''
    Class for an exoring system. Can be initialised with radii and tau, or empty.
    Each single ring (called a segment) consists of a radius and an optical depth tau.

    Segments are stored in strictly increasing radius r.

    Starting at r=0, the first segment goes out to r with constant optical depth tau.
    The next segment starts at the previous inner radius out to the next tau, and so on.

    Optical depth is defined as:

    tau = ln(I_ring/I_0) = -ln T

    ...which can be rearranged to:

    T = exp(-tau)

    T is the transmission (from 1 to 0)

    tau is from 0 to +inf, I_0 is incident flux behind the ring, I_ring is the 
    flux emerging from the ring towards the observer.

    '''
    def __init__(self, new_radii=None, new_tau=None):
        self.segments = Table(names=('radius','tau'), dtype=('f4','f4'))
        # PROBLEM: I want to initialise the Table with new_segments if they're specified
        # but I don't want to duplicate the Table creation. I need a command to add the
        # two columns specified in 
        if new_radii is not None:
            self.segments = Table([new_radii, new_tau], names=('radius','tau'), dtype=('f4','f4'))
            self.segments.sort(['radius'])
        
    def getRadius(self):
        return self.segments['radius']

    def getTau(self):
        return self.segments['tau']

    def addRing(self, segment):
        '''add a ring segment at outer radius r with transmission tau'''
        self.segments.add_row(segment)
        self.segments.sort(['radius'])

    def delRing(self, r):
        '''delete the ring segment closest to the input radius r'''
        dist = np.abs(self.segments['radius'] - r)
        self.segments.remove_row(np.argmin(dist))
        
    def showRing(self, outer_radius = 20, outer_tau = 0.0):
        '''
        returns (r,t) array suitable for plotting with plt.step()
        
        Example:
            p = Ring(5-np.arange(5),np.arange(5)*0.1)
            (r,t) = p.showRing()
            plt.step(r,t, where='pre', zorder=-10)
        '''
        r = np.append(np.insert(self.getRadius(),0,0),outer_radius)
        t = np.append(np.insert(self.getTau(),0,self.getTau()[0]),outer_tau)

        return(r,t)
        # draw the ring edges
        #ax.step(r, t, where='pre', zorder=-10)
    
    def _tau_to_T(tau):
        return(-np.ln(tau))

    def _T_to_tau(T):
        return(np.exp(-T))
