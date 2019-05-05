import numpy as np
from scipy.optimize import minimize, fmin
#import matplotlib as plt
import array
import consumer as con
#import producer as prod

class Economy(object):
	
"""the object is to find factor and goods prices 
that make the difference of goods provided by the producer and goods demanded by the consumer,
and the factors provided by the consumer and factors demanded by the producer to be 0"""

  def __init__ (self, askCon, askProd,noOfGoods,noOfFactos):
    self.askCon = askCon
    self.askProd = askProd
    self.noOfGoods = noOfGoods
    self.noOfFactors = noOfFactors
    #self.noOfCon = NoOfCon
    #self.noOfProd = NoOfProd
 
  def objective (self, inputList, no): 
		
 """In order to obtain maximized values from the above mentioned classes,
    prices for each good and factors need to be provided.
    The consumer also needs to know about the profit""" 
  
  
  p = numpy.array(inputList[0:self.noOfGoods]) 
  r = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors]) 
  prodProfit = numpy.empty(len(askProd))

 """ We start with the producer first in order to obtain the profit we will need for the consumer"""
  
  #Producer problem
	
  sumProdGoods = 0 
  sumProdFactors = 0 
        
    for i in self.askProd :
      j = 0 
      answerProd = self.i.maxProfit (p,r) 
      sumProdGoods += answerProd[0:self.noOfGoods] 
      sumProdFactors += answerProd[self.noOfGoods: self.noOfGoods+ self.noOfFactors] 
      prodProfit[j] = answerProd [noOfGoods+noOfFactors]
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

 #Consumer Problem

 sumConGoods = 0 
 sumConFactors = 0 
	 
    for i in self.askCon:
	
	answerCon =self.i.maxUtility (conProfit[j],p,r )
	sumConGoods += answerCon [0:self.noOfGoods]
	sumConGoods += answerCon[self.noOfGoods: self.noOfGoods+ self.noOfFactors]

	return sqrt(sumConGoods - sumProdGoods) 
        return sqrt(sumConFactors - sumProdFactors)
	      
 
# Find prices and wages that minimize to 0 this difference
#Try or guesses
p = numpy.ones(inputList[0:self.noOfGoods])
r = numpy.ones(inputList[0:self.noOfGoods])
print objective (p,r)

sol = minimize (objective, p,r, method ='SLSQP')

print (sol) 
  


