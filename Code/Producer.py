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

      for i in range (0,len(Vhf)):
        factorSupplyArray [i] = self.parameterDict["psi"]*math.pow((r[i]*Vhf[i]),(1-self.parameterDict["xi"]))/(1-self.parameterDict["xi"])
          
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

      profits =sumGoodBudget - sumFactorProfit

      return (-1)*profits


#maximization
    def maxProfit (self,r,p):
      profitCon = {'type' : 'eq', 'fun' : self.prodtFct, 'args' : (p,r)}
      constraint = [profitCon]
      solution = minimize(self.profitFct, guess, args = (p,r), method = 'SLSQP', constraints = constraint)
      sol = numpy.empty(self.noOfGoods+self.noOfFactors+1)
      for i in range (0, self.noOfGoods+self.noOfFactors+1):
          if i < (self.noOfGoods +self.noOfFactors):
              sol[i] = solution.x[i]
          else :
              sol[i] = solution.fun
      return sol


dict_obj = {
"xi" : 2,
"psi" : 0.5
}
producer = Producer(1,2,2,dict_obj,'cadires')

pi = 10
p = [1,7]
r = [4,9]

guess = [5,9,34,8]

print producer.prodtFct(guess,p,r)
print producer.profitFct(guess,p,r)
x = producer.maxProfit(r,p)
print x
print producer.profitFct(x,p,r)
