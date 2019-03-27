
import numpy
from scipy.optimize import minimize 


#This class models the consumers and their preferences of the economy

class Consumer (object):

    #This is the constructor for the consumer class, it provides the consumer object with all the parameters needed to calculate the utility function
    #alpha, beta, gamma, sigma and theta are parameters of the utility function
    
    def __init__ (self, noOfGoods, noOfFactors, alpha, beta, gamma, sigma, theta):
        self.noOfGoods = noOfGoods
        self.noOfFactors = noOfFactors
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.sigma = sigma
        self.theta = theta


    #This function calculates the utility for the consumer object the parameteres specified in the object
    #and the amount of consumed goods (Xhg) and factors supply (Vhf)
    #Xhg and Vhf are both one dimensional arrays with length of the number of goods / factors for this specific consumer

    
    def utilityFunction (self,inputList):

        #seperate good array (Xhg) from factor array (Vhf) goods come first
        Xhg = numpy.array(inputList[0:self.noOfGoods])
        Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])

        #goods part of utility function
        unsummed_goodU = numpy.empty(len(Xhg))
        j = 0
        for j in range(0,len(Xhg)):
            unsummed_goodU[j] = self.alpha * (Xhg[j] ** self.gamma)
        sum_goodU = 0
        i = 0
        for i in range(0,len(unsummed_goodU)):
            sum_goodU += unsummed_goodU[i]
        goodUtility = sum_goodU ** ((1-self.sigma)/self.gamma)

        #factor part of the utility function
        unsummed_factorU = numpy.empty(len(Vhf))
        j = 0
        for j in range(0,len(Vhf)):
            unsummed_factorU[j] = self.beta * ((Vhf[j]**(self.theta+1))/(self.theta + 1))
            
        sum_factorU = 0
        i = 0
        for i in range(0,len(unsummed_factorU)):
            sum_factorU += unsummed_factorU[i]

            factorUtility = sum_factorU


        #combining both parts to calculate utiliy
        utility = goodUtility - factorUtility

        return utility

    def invertedUtility (self, inputList, args):
        return (-1)*self.utilityFunction(inputList)

    #This function models the budget restriction of the consumer which is determined
    #by prices of goods(p) and factors (r) as well as the profit the consumer gets
    #allocated with (pi). This is an equality constraint where budget = 0. 
    
    def constraint(self, pi, p, r, Xhg, Vhf):

        # r*Vhf for every factor
        factorArray = numpy.empty(len(r))
        for i in (0, range(factorArray)):
            factorArray[i] = r[i]*Vhf[i]

        #sum of income through factors for consumer
        sumFactorBudget = 0
        for k in (0, range(factorArray)):
            sumFactorBudget += factorArray[k]

        #p*Xhg for every good
        goodArray = numpy.empty(len(p))
        for j in (0, range(len(goodArray))):
            goodArray[j] = p[j]*Xhg[j]

        #sum of money spent on goods for consumer
        sumGoodBudget = 0
        for l in (0, range(len(goodArray))):
            sumGoodBudget += goodArray[l]
            
        budget = sumFactorBudget - sumGoodBudget + pi
        
    #This function maximizes the utility function for a given pi, p and r
    def maxUtility(self, pi, p, r, guess):
        budgetCon = {'type' : 'eq', 'fun' : self.constraint}
        constraint = [budgetCon]
        solution = minimize(self.invertedUtility, guess, constraint)
        return solution.x
