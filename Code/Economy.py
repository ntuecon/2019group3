import numpy as np
from scipy.optimize import minimize, fmin
#import matplotlib as plt
import array
import consumer as con
import producer as prod

class Economy(object):
 
""" When asked, CON and PROD both give arrays with columns. 
the first for maximized goods, the second for maximized factors.
producer adds a profit as the third column."""

  def __init__ (self, askCon, askProd,noOfGoods,noOfFactos):
    self.askCon = askCon
    self.askProd = askProd
    self.noOfGoods = noOfGoods
    self.noOfFactors = noOfFactors
    #self.noOfCon = NoOfCon
    #self.noOfProd = NoOfProd
 
  def objective (self, inputList, no):
 """First we need to obtain maximized values from the other classes
    We ask the producer first in order to obtain the profit we will need for the consumer"""

	  p = numpy.array(inputList[0:self.noOfGoods])
   r = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors]) 
   
	  prodProfit = numpy.empty(len(askProd))
   sumProdGoods = 0
        
   for i in self.askProd :
		  j = 0
		  answerProd = self.i.maxProfit (p,r) #This will import an array from Ricky's Code given an p and an r.
		  sumProdGoods += answerProd [no] #takes the first argument, column, of the array, and updates the sum everytime an instance is given.
		  prodProfit[j] = answerProd [noOfGoods+noOfFactors] #takes the third argument, column, of the array and updates the sum everytime an instance is given.
		  j += 1
		
	 #Redistribution of profit
	 conProfit = numpy.empty(len(askCon))
	 for i in self.askCon :
		 j = 0
		 if i.noOfProd == 0 :
			 conProfit[j] = 0
		 else :
			 conProfit[j] = prodProfit[i.noOfProd-1]
		 j += 1


	 sumConGoods = 0

	 #Consumer Problem
	 for i in self.askCon:
		 j = 0
		 answerCon =self.i.maxUtility (conProfit[j],p,r )
		 sumConGoods += askCon [no]

	return sqrt(sumConGoods - sumProdGoods)
      
   
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
  

