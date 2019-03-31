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
x0 = [1,2]
  
#We need to find the minimum 
#Option 1 = the curve_fit method will only find the nearest local minimum (greedy method)
#For goods

print optimization.curve_fit(sqrt_excess_goods_f, CON, PROD, x0)

#For factors
print optimization.curve_fit(sqrt_excess_factors_f, CON, PROD, x0)

#if we use this method, we will have to read and input the results to find total utility, now assuming more than one
class total_utility (CON, PROD):
  for i in range [0,len(CON)]:
  ResultForGoods = raw_input("Where is the minimum value")
  TotalGoods = 0
  TotalGoods += ResultForGoods
  ResultForFactors = raw_input ("Where is the minimum value")
  TotalFactors = 0
  TotalFactors += ResultForFactors
  together = [TotalGoods,TotalFactors]

  def GlobalUtility (together):
  global_utility = together.maxUtility(pi,p,r,guess)
  return global_utility
  print "%s is the amount of happiness of this society" %global_utility

