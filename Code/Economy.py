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
    
  p = numpy.array(inputList[0:self.noOfGoods]) #creates an array that is the lenght of the Number of goods.
  r = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors]) #creates an array that is the lenght number of factors.
  prodProfit = numpy.empty(len(askProd)) #creates an empty array that is the length of the producer's answer. Do I have to write self here? Why or why not?
	
 """ We start with the producer first in order to obtain the profit we will need for the consumer"""
  
  #Producer problem
	
  sumProdGoods = 0 #We need to sum the good values provided by every producer.
  sumProdFactors = 0 #We need to sum the factor values provided by every producer.
        
    for i in self.askProd :
      j = 0 #I do not know why we did this.
      answerProd = self.i.maxProfit (p,r) #This will import THE input list from Ricky's Code given an p and an r.
      sumProdGoods += answerProd[0:self.noOfGoods] #creates an array with the sum of all the goods items of the producers answer and updates the sum everytime its instantiated.
      sumProdFactors += answerProd[self.noOfGoods: self.noOfGoods+ self.noOfFactors] #creates an array with the sum of all the factor items of the producers answer and updates the sum everytime its instantiated.
      prodProfit[j] = answerProd [noOfGoods+noOfFactors] #takes the last value of the producer's answer, that is the profit.
      j += 1 #I do not know why we did this.
		
	 #Redistribution of profit
	 conProfit = numpy.empty(len(askCon)) #creates an empty array the length of the askCon list.
	 for i in self.askCon : #This loop looks for the consumers that are producers.
	   j = 0 #What is this for
	   if i.noOfProd == 0 : 
	     conProfit[j] = 0
           else :
	     conProfit[j] = prodProfit[i.noOfProd-1] #I do not understand this.
		 j += 1#What is this for

 #Consumer Problem

 sumConGoods = 0 #We need to sum the good values prefered by every consumer.
 sumConFactors = 0 #We need to sum the factor values provided by every consumer.
	 
    for i in self.askCon:
	answerCon =self.i.maxUtility (conProfit[j],p,r )
	sumConGoods += answerCon [0:self.noOfGoods]
	sumConGoods += answerCon[self.noOfGoods: self.noOfGoods+ self.noOfFactors]

	return sqrt(sumConGoods - sumProdGoods)
	return sqrt(sumConFactors - sumProdFactors)

      
 
 # Find prices and wages that minimize to 0 this difference



  


