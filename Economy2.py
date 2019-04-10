import numpy as np
from scipy.optimize import minimize, fmin
import matplotlib as plt
import array
import consumer as c
import producer as p

class market_clearing ():
 
""" When asked, CON and PROD both give arrays with columns. 
the first for maximized goods, the second for maximized factors.
producer adds a profit as the third column."""

  def __init__ (self):
    self.askCon = askCon
    self.askProd = askProd
    self.NoOfCon = NoOfCon
    self.NoOfProd = NoOfProd
 
  def objective ():
 """First we need to obtain maximized values from the other modules
    We ask the producer first in order to obtain the profit we will need for the consumer"""
      
      SumProdGoods = 0
      SumProdProfit =0
      askProd = self.p[i].maxProfit (p,r) #This will import an array from Ricky's Code given an p and an r.
      SumProdGoods = askProd [0] #takes the first argument, column, of the array, and updates the sum everytime an instance is given.
      SumProdProfit = askProd [2] #takes the third argument, column, of the array and updates the sum everytime an instance is given.
      
      SumConGoods = 0
      askCon =self.p[i].maxUtility (p,r, SumProdProfit)
      SumConGoods = askCon [0]
      
   
#For ONE good and one factor, we need to get the respective values for X and V so as to see the difference (excess demand or supply)
#For goods

    def sqrt_excess_goods_f (SumProdGoods, SumConGoods):
        sqrt_excess_goods = (SumProdGoods [0] - SumConGoods [0])**2
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
  






