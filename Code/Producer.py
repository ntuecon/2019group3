import numpy
from scipy.optimize import minimize


class Producer (object):
    """ This class models the producer """

    def __init__ (self,noProducer, noOfGoods, noOfFactors, parameterDict,producedGood):
      """ This is the constructor for the producer class, it provides the consumer object with all the parameters
          needed to calculate the profit, as well as the link to which producers profit. 
          noOfProducer : number that indicates which producers profit will go to this consumer, 0 if no producers profit goes
          to this consumer
          noOfGoods, noOfFactors : number of goods and factors in this economy 
          parameterDict : dictonary that contains all parameters that define the production function (Fi= total of goods, Xi,Psi) )
          producedGood : which good will be produced by the producer"""
      
      self.noProducer = noProducer
      self.noOfGoods = noOfGo
      self.noOfFactors = noOfFactors
      self.parameterDict = parameterDict
      self.producedGood = producedGood
        
        
        
        

#constraint
      def prodtFct (inputList,p,r):
        #seperate good array (Xhg) from factor array (Vhf) goods come first
        Xhg = numpy.array(inputList[0:self.noOfGoods])
        Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])

        factorSupplyArray = numpy.empty(len(r))

        for i in range (0,len(Vhf)):
            factorSupplyArray [i] = self.parameterDict["psi"][i]*(Vhf[i]**(1-self.parameterDict["xi"])/(1-self.parameterDict["xi"])

        sumFactorSupply = 0
        for j in range (0,len(factorSupplyArray)):
            sumFactorSupply += factorSupplyArray[j]


        sumGoods = 0
        for x in range (0,len(Xhg)):
            sumGoods += Xhg[x]

        return sumFactorSupply - sumGoods                                                       
#objective
      def profitFct (Xhg, Vhg):
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
        

        profits =sumGoodprofit - sumFactorprofit

        return (-1)*profits


#maximization
      def maxProfit (r,p):

          """ This function maximizes the profit function for a given pi, p and r. """
    
        ProfitCon = {'type' : 'eq', 'fun' : self.constraint, 'args' : (p,r,)}
        constraint = [profitsCon]
        solution = minimize(self.profitFct, guess, args = (p,r), method = 'SLSQP', constraints = constraint)
        return solution.x

                                                                  
