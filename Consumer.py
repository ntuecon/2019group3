
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
    
    def utilityFunction (self, inputList):

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


        #combining both parts to calculate utiliy
        utility = sum_goodU + sum_factorU

        return utility

    def invertedUtility (self, inputList):
        return (-1)*utilityFunction (inputList)

    #This function models the budget restriction of the consumer which is determined
    #by prices of goods(p) and factors (r) as well as the profit the consumer gets
    #allocated with (pi). This is an equality constraint where budget = 0. 
    
    def constraint(pi, p, r, Xhg, Vhf):

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
        con = [budgetCon]
        solution = minimize(self.invertedUtility, guess, con)
        return solution
    

#Testing the utility function
print "---------------TEST-----------------"

#consumation of goods (here 5 goods)
X = numpy.array([4,6,3,1,7])
print "Good Allocation"
print X
print len(X)
i = 0

#use of factors (here 7)
V = numpy.array([1,2,6,2,3,6,8])
print "Factor Use"
print V
print len(V)

#create a big input array
inputList = [4,6,3,1,7,1,2,6,2,3,6,8]
print "input Array"
print inputList
print len(inputList)

#create consumer
c1 = Consumer(5,7,0.5,0.3,0.8,0.2,0.8)
print "Consumer Parameter"
print c1.alpha
print c1.beta
print c1.gamma
print c1.sigma
print c1.theta

#calculate utiltiy of the consumer
resultU = c1.utilityFunction(inputList)

print "RESULT"
print resultU

#test maximization
print "TEST MAXIMIZATION--------------------------"

#create parameters
p = [3,6,4]
r = [2,9,2,7]
pi = 14
guess =[0,0,0,0,0,0,0]

sol = c1.maxUtility( pi,p,r,guess)

print (sol)


            
