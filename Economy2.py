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


#OPTION 2 = Nelder-Mead Simplex algorithm "because it does not use any gradient evaluations, it may take longer to find the minimum."
#For one

def mimimization ():

  res1 = minimize(sqrt_excess_goods_f, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
  result1= res1.x
  res2 = minimize(sqrt_excess_factors_f, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
  result2= res2.v

#For many

class AllUtility():
  CON = maxUtility (pi, p, r)
  PROD = maxProfit (pi, p, r)
    def sqrt_excess_goods_f (CON, PROD)
      for i in CON:
        for i in PROD:
        resultA= (CON [0][i] - PROD [0][i])**2
        goods =0
        goods += resultA
        return goods 
  
    def sqrt_excess_factors_f (CON,PROD)
       for i in CON:
         for i in PROD:
         resultB= (CON [1][i] - PROD [1][i])**2
         factors =0
         factors += resultb
         return factors
  
  
     yiqi = all_utility(goods,factors)

    def UniversalUtility (together):
    universe_utility = yiqi.maxUtility(pi,p,r,guess)
    return universe_utility
    print "%s is the amount of happiness of this society" %universe_utility



  






