import numpy as np
from scipy.optimize import minimize, fmin
import matplotlib as plt
from sympy import *
import array

# When asked, CON and PROD both give arrays with columns. 
# the first for maximized goods, the second for maximized factors.
# producer adds a profit as the third column.

class market_clearing (Consumer, Producer):
 
#We define those variables that are inherit from the Consumer, MIchelle's Code, and Producer, Ricky's code class.

 p = 0
 r = 0
 AskProd = maxProfit (self,p,r)
 #Depending on Producers result, get pi.
 pi = maxProfit.pi
 AskCon = maxUtility(self, pi, p, r)
      
   
#For ONE good and one factor, we need to get the respective values for X and V so as to see the difference (excess demand or supply)
#For goods

    def sqrt_excess_goods_f (AskProd, AskCon):
        sqrt_excess_goods = (AskCon [0] - Askprod [0])**2
        return sqrt_excess_goods
        print str(sqrt_excess_goods)


#For factors
        
    def sqrt_excess_factors_f (AskCon,AskProd):
        sqrt_excess_factors = (AskCon [1] - AskProd [1])**2
        return sqrt_excess_factors
        print str(sqrt_excess_factors)
 
 # Find prices and wages that minimize to 0 this difference



  
  together = total_utility(TotalGoods,TotalFactors)

  def GlobalUtility (together):
    global_utility = together.maxUtility(pi,p,r,guess)
    return global_utility
  print "%s is the amount of happiness of this society" %global_utility
  






