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
        print "INPUTLIST ECONOMY:"
        print inputList
        p = numpy.array(inputList[0:self.noOfGoods])
        r = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])
        prodProfit = numpy.empty(len(self.askProd))

        consumedArray = numpy.empty(self.noOfGoods+self.noOfFactors)
        producedArray = numpy.empty(self.noOfGoods+self.noOfFactors)
        for no in  range (0, self.noOfGoods+self.noOfFactors):
            consumedArray[no] = 0
            producedArray [no] = 0
        
        #Producer problem

        for i in self.askProd :
            j = 0
            answerProd = i.maxProfit (p,r)
            for no in  range (0, self.noOfGoods+self.noOfFactors):
                producedArray[no] += answerProd[no]
                prodProfit[j] = answerProd [self.noOfGoods+self.noOfFactors]*(-1)
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
            print "RESULT of Market Clearance: " + srt(i)
            print result

        return result


              
    #positivity condition
    def constraint(self, inputList,no):
        return inputList[no]
        
    def findEquilibrium(self):
        """ This method calculates the prices for which the respective economy is in an equilibrium """
    
        print "-------------------FIND EQUILIBRIUM------------------------"
        # Find prices and wages that minimize to 0 this difference
        #Try or guesses
        guess = numpy.empty(self.noOfGoods + self.noOfFactors)
        for i in range (0,self.noOfGoods+self.noOfFactors):
            guess[i] = 5

        #positivity constraints
        constraintPos = [{}]*(self.noOfGoods + self.noOfFactors)
        for no in range (0, self.noOfGoods+self.noOfFactors):
            con = {'type' : 'ineq', 'fun' : self.constraint, 'args' :[no]}
            print str(no) + "NO ECONOMY POSITIVITY CONSTRAINT"
            constraintPos[no] = con
            
        
        sol = minimize (self.objective,guess,args = ( ) , method ='SLSQP', constraints = constraintPos)
        

        return sol

    def getIncome(self, p,r):
        """ This method calculates the income of consumers and returns them in an array for given prices """
        #array to save all incomes of consumers
        valueArray = numpy.empty(len(self.askCon))

        #calculate the profit of producers 
        prodProfit = numpy.empty(len(self.askProd))
        #for every producer calculate the profit for given p and r
        for i in self.askProd :
            j = 0
            answerProd = i.maxProfit (p,r)
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
        
        #calculate the income of consumers for the optimal prices p,r
        j = 0
        for i in self.askCon:
            answerCon = i.maxUtility (conProfit[j],p,r)
            print "INCOME"
            #calculate the budget the consumer gets from supplying factors
            for m in range(self.noOfGoods,self.noOfGoods+self.noOfFactors):
                print answerCon[j]
                print r[m-self.noOfGoods]
                valueArray[j] += answerCon[j]*r[m-self.noOfGoods]
                print valueArray[j]
            #adding budget from the profit gained of producers
            valueArray[j] += conProfit[j]*(-1)
            j+=1
        print conProfit[0]

        print "VALUE"
        print valueArray[0]

        return valueArray


    
    def calculateGini(self, valueArray):
        """ This method calculates the gini coefficient of the repective economy"""
    
        
        #calculate gini coefficent with the help of this script https://planspacedotorg.wordpress.com/2013/06/21/how-to-calculate-gini-coefficient-from-raw-data-in-python/

        valueArray = sorted(valueArray)
        height, area = 0,0
        for value in valueArray:
            height += value
            area += height - value / 2.
        fair_area = height * len(valueArray)
        return (fair_area - area) / fair_area



    def s80_s20 (self, valueArray):
        """ This method returns the S80/S20 measure of the respective economy"""

        valueArray = sorted(valueArray)
        quantil = len(valueArray)/5
        quantil = round(quantil,0)

        #calculate income of poorest 20 percent
        sumPoor = 0
        for i in range(0,quantil):
            sumPoor += i

        #calculate income of richest 20 percent
        sumRich = 0
        for i in range(len(valueArray)-quantil, len(valueArray)):
            sumRich += i

        return sumRich/sumPoor
