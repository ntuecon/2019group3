#Here we try to find the equilibrium, and the value of the factors to clear the market.

import numpyp as np
from spicy.optimize import minimize

"""We import from simpy so that we can do symbolic math. That means python will read our letters as symbols
because that is how we defined the variables"""

from sympy import *
Xhg  = symbols('Xhg')
Vhf = symbols('Vhf')

"""We want to maximize the sum of the utilities or use the utilitarian approach
, subject to the constant utilities of all other individuals and the quantity
available, that is dependent on the production function"""


#Assumption 1: the more goods the better
# We take the utilitarian Social Welfare function
W [U^h (Xhg ; Vhf )] = SUM from h=1 to H  U^h (Xhg ; Vhf )


class market_clearence (Xhg, Vhf) :
 
 if demand - supply = 0
  return "market cleared"

 if excess_demand == 0
  return "market cleared"

 else:
  return "unable to clear market"

  result = []
  for in 
  append 
  return result



#We want to maximize the utility, subject to some contraints.


#from grou p 2018 
 def utility_max(self):
        import numpy as np
        from scipy.optimize import minimize
        """
        1.The package of minimize can be use as maximize ,if the
        objective function is multiply by -1.
        2."cons" set as the constrain of optimization problem.
        3.If we use SLSQP method, the jacobian of objective function is necessary.
        The jacobian means the partial derivative of every independent variables. 
        """
        #GFvec=[[]]*(self.ng+self.nf)
        """res = minimize(self.utility, np.ones(self.ng+self.nf), args=(-1.0,),"""
        res = minimize(self.utility, [10.0]*(self.ng+self.nf), args=(-1.0,),
                       constraints=self.cons(), method='SLSQP', options={'disp': True})
        return res.x
       

       #Testing the economy 
print "---------------TEST-----------------"

#We want to maximize the welfare
max W ( U (Xhg (+) , V1f (-) ) )

Class utility (self):

### from 2018groupCE
 """X=   [v1,v2,...vH,
                x11,x21,...,xG1,f11,f21,...fF1,
                x12,x22,...,xG2,f12,f22,...fF2,
                .
                .
                .
                x1H,x2H,...,xGH,f1H,f2H,...fFH,
                r11,r12,...,r1F,r21,r22,...,r2F,....,rG1,rG2,...,rGF,rV1,rV2,...,rVF]"""
                
                
### from 2018groupCE
class Social_Welfare(object):

    def __init__(self,consumers,producers):
        self.consumers=consumers #list of consumers
        self.producers=producers #list of producer
                
                
### from 2018groupCE
def __call__(self, X): 
        '''
        i=0,1,2,...,H
        This makes the utility function a callable function
        '''


