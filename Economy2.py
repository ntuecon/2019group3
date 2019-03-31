import numpy as np
from scipy.optimize import minimize, fmin
import matplotlib as plt
from sympy import *

#We initialize 

#where Xg1 and V are the maximized goods and factors by the consumers according to their utility (Michelle)
#and Xg2 and V2 are maximed production of goods produced by the factors given by the profit function (Ricky)


class market_clearing ():
 
  pi = symbols ('pi')
  p = symbols ('p')
  r = symbols ('r')
  
  """where CON is the consumer allocation, an array with two columns, the first for goods, the second for factors,
  and the rows are the number of consumers"""
  """where PROD is the producer prefered allocation, an array with two columns, the first for goods, the second for factors,
  and the rows are the number of producers"""
  
  CON = maxUtility (pi, p, r)
  PROD = maxProfit (pi, p, r)
  
#For ONE consumer and one producer, we need to get the respective values for X and V so as to see the difference (excess demand or supply)
#For goods

def sqrt_excess_goods_f (CON, PROD)
  return (CON [0] - PROD [0])**2

#For factors
def sqrt_excess_factors_f (CON,PROD)
  return (CON [1] - PROD [1])**2

#Initial guess
x0 = np.array[1,2]

#If we were to do it for MORE THAN 1, maybe like this? I don't know if it will do it in order, and if so, how to make sure it does.
def sqrt_excess_goods_f (CON, PROD)
for i in CON:
 for i in PROD:
   return (CON [0][i] - PROD [0][i])**2
  
def sqrt_excess_factors_f (CON,PROD)
for i in CON:
 for i in PROD:
   return (CON [1][i] - PROD [1][i])**2
  
  #Initial guess
x0 = np.array[[1,2,3,4],[1,2,3,4]]




#Now the minimum point 
#OPTION 1 = the curve_fit method. It will only find the nearest local minimum (greedy method), but it will graph it, yay.
#For goods

print optimization.curve_fit(sqrt_excess_goods_f, CON, PROD, x0)

#For factors
print optimization.curve_fit(sqrt_excess_factors_f, CON, PROD, x0)

#if we use this method, we will have to read from the graph and input the results to find total utility
#this should work for more than one producer and one consumer
class total_utility (CON, PROD):
  for i in range [0,len(CON)]:
    ResultForGoods = raw_input("Where is the minimum value")
    TotalGoods = 0
    TotalGoods += ResultForGoods
    return TotalGoods
  for i in range [0,len(CON)]:
    ResultForFactors = raw_input ("Where is the minimum value")
    TotalFactors = 0
    TotalFactors += ResultForFactors
    return TotalFactors
  
  together = total_utility(TotalGoods,TotalFactors)

  def GlobalUtility (together):
  global_utility = together.maxUtility(pi,p,r,guess)
  return global_utility
  print "%s is the amount of happiness of this society" %global_utility
  
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





