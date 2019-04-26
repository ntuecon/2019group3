

import numpy
from scipy.optimize import minimize


class Producer (object):
    """ This class models the producer """

     def __init__ (self,noProducer, noOfGoods, noOfFactors, parameterDict):
        """ This is the constructor for the producer class, it provides the consumer object with all the parameters
            needed to calculate the profit, as well as the link to which producers profit. 
            noOfProducer : number that indicates which producers profit will go to this consumer, 0 if no producers profit goes
            to this consumer
            noOfGoods, noOfFactors : number of goods and factors in this economy 
            parameterDict : dictonary that contains all parameters that define the production function (Fi= total of goods, Xi,Psi) )  """
        
        self.noProducer = noProducer
        self.noOfGoods = noOfGo
        self.noOfFactors = noOfFactors
        self.parameterDict = parameterDict
        Self.fi = fi
        Self.xi = xi
        Self.psi = psi
        
        Fi =Sumatori *gf*(((r*gf)^1-Xig)/(1-Xig)
        

#constraint
        def prodtFct (r)
        """ This function calculates the production function """

        
         #seperate good array (Xhg) from factor array (Vhf) goods come first
        Xhg = numpy.array(inputList[0:self.noOfGoods])
        Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])
        
    


#objective
        def profitFct (Xhg, Vhg)
        """ In this section we define the profit function of producers"""
        
        Xhg = numpy.array(inputList[0:self.noOfGoods])
        Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])

             #p*Xhg for every good
        goodArray = numpy.empty(len(p))
        for j in range(0,len(goodArray)):
            goodArray[j] = p[j]*Xhg[j]

        #sum of money spent on goods for consumer
        sumGoodBudget = 0
        for l in range(0,len(goodArray)):
            sumGoodprofit += goodArray[l]

         # r*Vhf for every factor
        factorArray = numpy.empty(len(r))
        for i in range(0,len(factorArray)):
            factorArray[i] = r[i]*Vhf[i]

        #sum of income through factors for consumer
        sumFactorProfit = 0
        for k in range(0,len(factorArray)):
            sumFactorprofit += factorArray[k]
     

        # Total profits = Xhg*p + r *Vhf
            

            profits = sumFactorprofit - sumGoodprofit

        return profits
    

#maximization
        def maxProfit (r,p)

         """ This function maximizes the profit function for a given pi, p and r. """
        
        ProfitCon = {'type' : 'eq', 'fun' : self.constraint, 'args' : (pi,p,r,)}
        constraint = [profitsCon]
        solution = minimize(self.inverted, guess, args = (pi,p,r), method = 'SLSQP', constraints = constraint)
        return solution.x
                    
       

