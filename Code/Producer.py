import numpy
from scipy.optimize import minimize
import math

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
      self.noOfGoods = noOfGoods
      self.noOfFactors = noOfFactors
      self.parameterDict = parameterDict
      self.producedGood = producedGood
        

#constraint
    def prodtFct (self,inputList,p,r):
      #seperate good array (Xhg) from factor array (Vhf) goods come first
      Xhg = numpy.array(inputList[0:self.noOfGoods])
      Vhf = numpy.array(inputList[self.noOfGoods : self.noOfGoods+self.noOfFactors])

      factorSupplyArray = numpy.empty(len(r))
      

      for i in range(0,len(r)):
          if Vhf[i] >= 0:
              factorSupplyArray[i] = self.parameterDict["psi"]*(math.pow((Vhf[i]),(1-self.parameterDict["xi"]))/(1-self.parameterDict["xi"]))
          else :
              factorSupplyArray[i] = -100000
          
      sumFactorSupply = 0
      for j in range (0,len(factorSupplyArray)):
          sumFactorSupply += factorSupplyArray[j]

      sumGoods = 0
      for x in range (0,len(Xhg)):
          sumGoods += Xhg[x]

      return sumFactorSupply - sumGoods
    
#objective
    def profitFct (self,inputList, p, r):
        
      
      Xhg = numpy.array(inputList[0:self.noOfGoods])
      Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])
      #print " INPUTLIST PRODUCER"
      #print inputList

  
      #p*Xhg for every good
      goodArray = numpy.empty(len(p))
      for j in range(0,len(goodArray)):
          goodArray[j] = p[j]*Xhg[j]


      #sum of money spent on goods for consumer
      sumGoodBudget = 0
      for l in range(0,len(goodArray)):
          sumGoodBudget += goodArray[l]

        # r*Vhf for every factor
      factorArray = numpy.empty(len(r))
      for i in range(0,len(factorArray)):
          factorArray[i] = r[i]*Vhf[i]

      #sum of income through factors for consumer
      sumFactorProfit = 0
      for k in range(0,len(factorArray)):
          sumFactorProfit += factorArray[k]
          


      # Total profits = Xhg*p - r *Vhf      

      profits = sumGoodBudget - sumFactorProfit

      return (-1)*profits

#positivity condition
    def constraint(self, inputList,no):
        return inputList[no]

#maximization
    def maxProfit (self,p,r):

        print "----------START SOLVING PRODUCER PROBLEM--------"
        x = len(p)+len(r)
        guess = numpy.empty(x)
        for i in range(0,x):
            guess[i] = 100
            
        profitCon = {'type' : 'eq', 'fun' : self.prodtFct, 'args' : (p,r)}
        constraint = [profitCon]
        """
        constraint = [{}]*(self.noOfGoods + self.noOfFactors +1)
        constraint[0] = profitCon
        for no in range (0, self.noOfGoods+self.noOfFactors ):
            con = {'type' : 'ineq', 'fun' : self.constraint, 'args' :[no]}
            print str(no) + "NO Positivity Constraint"
            constraint[no+1] = con
        """
        solution = minimize(self.profitFct, guess, args = (p,r), method = 'SLSQP', constraints = constraint)

        print "Proft Producer"
        print solution.fun

        sol = numpy.empty(self.noOfGoods+self.noOfFactors+1)
        for i in range (0, self.noOfGoods+self.noOfFactors+1):
            if i < (self.noOfGoods +self.noOfFactors):
                sol[i] = solution.x[i]
            else :
                sol[i] = (-1)*solution.fun
                
        print sol
        return sol
