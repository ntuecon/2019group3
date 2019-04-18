
import numpy
from scipy.optimize import minimize 




class Consumer (object):
    """ This class models the consumers and their preferences of the economy """

    
    
    
    def __init__ (self,noProducer, noOfGoods, noOfFactors, parameterDict):
        """ This is the constructor for the consumer class, it provides the consumer object with all the parameters
            needed to calculate the utility function, as well as the link to which producers profit the consumer will obtain
            as part of his budget. 
            noOfProducer : number that indicates which producers profit will go to this consumer, 0 if no producers profit goes
            to this consumer
            noOfGoods, noOfFactors : number of goods and factors in this economy 
            parameterDict : dictonary that contains all parameters that define the utiliy function (alpha, beta, gamma, theta, sigma)  """
        
        self.noProducer = noProducer
        self.noOfGoods = noOfGoods
        self.noOfFactors = noOfFactors
        self.parameterDict = parameterDict

    
    def utilityFunction (self,inputList):
        """ This function calculates the utility for the consumer object the parameteres specified in the object. 
            It needs the amount of each good and factor to calculate the consumers utility. The amount of goods consumed is given in the 
            array Xhg and the amount of factors provided in the array Vhf.
            Xhg and Vhf are both one dimensional arrays with length of the number of goods / factors for this specific consumer.
            This function returns one float that describes the amount of utiltiy for this consumer and this specific
            good/factor allocation"""
        
        #seperate good array (Xhg) from factor array (Vhf) goods come first
        Xhg = numpy.array(inputList[0:self.noOfGoods])
        Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])

        #goods part of utility function
        unsummed_goodU = numpy.empty(len(Xhg))
        j = 0
        for j in range(0,len(Xhg)):
            unsummed_goodU[j] = self.parameterDict["alpha"][j] * (Xhg[j] ** self.parameterDict["gamma"])
        sum_goodU = 0
        i = 0
        for i in range(0,len(unsummed_goodU)):
            sum_goodU += unsummed_goodU[i]
        goodUtility = sum_goodU ** ((1-self.parameterDict["sigma"])/self.parameterDict["gamma"])

        #factor part of the utility function
        unsummed_factorU = numpy.empty(len(Vhf))
        j = 0
        for j in range(0,len(Vhf)):
            unsummed_factorU[j] = self.parameterDict["beta"] * ((Vhf[j]**(self.parameterDict["theta"][j]+1))/(self.parameterDict["theta"][j] + 1))
            
        sum_factorU = 0
        i = 0
        for i in range(0,len(unsummed_factorU)):
            sum_factorU += unsummed_factorU[i]

        factorUtility = sum_factorU

        #combining both parts to calculate utiliy
        utility = goodUtility - factorUtility

        return utility

    def invertedUtility (self, inputList,pi,p,r):
        """ This function inverts the utility function so the scipy.minimize function can be used to solve our maximazation problem. """ 

        return (-1)*self.utilityFunction(inputList)


    
    def constraint(self,inputList, pi, p, r):
        """ This function models the budget restriction of the consumer which is determined by prices of goods(p)
            and factors (r) as well as the profit the consumer gets allocated with (pi). This is an equality constraint
            where budget must equal 0. Profit (pi) will be input as float. Prices (p,r) will be input as arrays which have
            the length of the respective number of goods and factors in the given economy. """ 
        
        Xhg = numpy.array(inputList[0:self.noOfGoods])
        Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])

        # r*Vhf for every factor
        factorArray = numpy.empty(len(r))
        for i in range(0,len(factorArray)):
            factorArray[i] = r[i]*Vhf[i]

        #sum of income through factors for consumer
        sumFactorBudget = 0
        for k in range(0,len(factorArray)):
            sumFactorBudget += factorArray[k]

        #p*Xhg for every good
        goodArray = numpy.empty(len(p))
        for j in range(0,len(goodArray)):
            goodArray[j] = p[j]*Xhg[j]

        #sum of money spent on goods for consumer
        sumGoodBudget = 0
        for l in range(0,len(goodArray)):
            sumGoodBudget += goodArray[l]
            
        budget = pi + sumFactorBudget - sumGoodBudget

        return budget


        
    
    def maxUtility(self, pi, p, r, guess):
        """ This function maximizes the utility function for a given pi, p and r. """
        
        budgetCon = {'type' : 'eq', 'fun' : self.constraint, 'args' : (pi,p,r,)}
        constraint = [budgetCon]
        solution = minimize(self.invertedUtility, guess, args = (pi,p,r), method = 'SLSQP', constraints = constraint)
        return solution.x


    

    

""" Testing the code above """ 

print "---------STARTING TEST------------------------------------------------------------"

dict = {
    "alpha" : [2,5],
    "beta" : 0.5,
    "gamma" : 2,
    "sigma" : 0,
    "theta" : [2,3]
    }

c = Consumer(1,2,2,dict)

pi = 10
p = [1,7]
r = [4,9]

guess = [5,9,34,8]

u = c.invertedUtility(guess, pi, p, r)

print "---------MAXIMIZED UTILITY FOR GIVEN BUDGET AND PRICES--------------------------"
print u

sol = c.maxUtility(pi,p,r,guess)

print "----------MAXIMIZED GOOD/FACTOR ALLOCATION FOR GIVEN BUDGET AND PRICES-----------"
print sol



