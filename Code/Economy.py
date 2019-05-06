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
    

    def objective (self, inputList, no):
        p = numpy.array(inputList[0:self.noOfGoods])
        r = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])
        prodProfit = numpy.empty(len(self.askProd))

        #Producer problem
        sumProd = 0  

        for i in self.askProd :
            j = 0
            answerProd = i.maxProfit (p,r)
            sumProd += answerProd[no]
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
            sumCon += answerCon [no]
            j += 1

        return pow(sumCon,2) - pow(sumProd,2) 
              

    def findEquilibrium(self):
        # Find prices and wages that minimize to 0 this difference
        #Try or guesses
        guess = numpy.empty(self.noOfGoods + self.noOfFactors)
        for no in range (0, self.noOfGoods+self.noOfFactors):
            sol = minimize (self.objective,guess,args = (no), method ='SLSQP')
            result = self.objective(sol.x,no)
            if result == 0:
                print "Good / Factor No: " + str(no) + " market is cleared"
            else :
                print "ERROR"

        return sol.x

