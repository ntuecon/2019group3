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


def gradient_descent ():
 askCon_current = askProd_current = 0
 iterations = 1000
 learning_rate = 0.0001
   for i in range (iterations):
     sqrt_excess_goods = (AskCon [0] - Askprod [0])**2
     AskConDer = 2 AskCon [0]
     AskConProd =2 Askprod [0]
     AskCon_current = askCon_current - learning_rate*AskConDer
     AskProd_current = AskProd_current - learning_rate*AskProdDer
     print ("AskCon[0][], AskProd[0][],iteration, sqrt_excess_goods ". format

   
#if we use this method, we will have to read from the graph and input the results to find total utility
#this should work for more than one producer and one consumer
  def total_utility (AskCon, AskProd):
    for i in range [0,len(AskCon)]:
      ResultForGoods = raw_input("At which p and r, is the difference 0")
      TotalGoods = 0
      TotalGoods += ResultForGoods
      return TotalGoods
     
    for i in range [0,len(AskProd)]:
      ResultForFactors = raw_input ("At which p and r, is the difference 0")
      TotalFactors = 0
      TotalFactors += ResultForFactors
      return TotalFactors
  
  together = total_utility(TotalGoods,TotalFactors)

  def GlobalUtility (together):
    global_utility = together.maxUtility(pi,p,r,guess)
    return global_utility
  print "%s is the amount of happiness of this society" %global_utility
  






