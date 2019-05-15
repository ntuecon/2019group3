from math import *
import numpy 
from scipy.optimize import minimize
import array
from Consumer import Consumer as con
from Producer import Producer as prod

class Economy(object):
	

    def __init__ (self, askCon, askProd, noOfGoods, noOfFactors):
        self.askCon = askCon
        self.askProd = askProd
        self.noOfGoods = noOfGoods
        self.noOfFactors = noOfFactors
    

    def objective (self, inputList):
        p = numpy.array(inputList[0:self.noOfGoods])
        r = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])
        prodProfit = numpy.empty(len(self.askProd))

        consumedArray = numpy.empty(self.noOfGoods+self.noOfFactors)
        producedArray = numpy.empty(self.noOfGoods+self.noOfFactors)

        
        #Producer problem 

        for i in self.askProd :
            j = 0
            answerProd = i.maxProfit (p,r)
            for no in  range (0, self.noOfGoods+self.noOfFactors):
                producedArray[no] += answerProd[no]
            prodProfit[j] = answerProd [self.noOfGoods+self.noOfFactors]
            j += 1

        #Redistribution of profit
        conProfit = numpy.empty(len(self.askCon))
        for i in self.askCon :
            j = 0
            if i.noProducer == 0 :
                conProfit[j] = 0
            else :
                conProfit[j] = prodProfit[i.noProducer-1]
            j += 1

        #Consumer Problem

        sumCon = 0

        j = 0
        for i in self.askCon:
            answerCon =i.maxUtility (conProfit[j],p,r )
            for no in  range (0, self.noOfGoods+self.noOfFactors):
                consumedArray[no] += answerCon [no]
            j += 1


        result = 0

        for i in range (0, self.noOfGoods+self.noOfFactors):
            result += pow(consumedArray[no]-producedArray[no],2)

        return result
              
    #positivity condition
    def constraint(self, inputList,no):
        return inputList[no]
        
    def findEquilibrium(self):
        # Find prices and wages that minimize to 0 this difference
        #Try or guesses
        guess = numpy.empty(self.noOfGoods + self.noOfFactors)
        #positivity constraints
        
        constraintPos = [{}]*(self.noOfGoods + self.noOfFactors)
        for no in range (0, self.noOfGoods+self.noOfFactors):
            con = {'type' : 'ineq', 'fun' : self.constraint, 'args' :[no]}
            print str(no) + "NO"
            constraintPos[no] = con
            
        
        sol = minimize (self.objective,guess,args = ( ) , method ='SLSQP', constraints = constraintPos)
        

        return sol.x


  


