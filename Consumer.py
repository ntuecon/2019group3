import numpy


#This class models the consumers and their preferences of the economy

class Consumer (object):

    #This is the constructor for the consumer class, it provides the consumer object with all the parameters needed to calculate the utility function
    #alpha, beta, gamma, sigma and theta are parameters of the utility function
    
    def __init__ (self, alpha, beta, gamma, sigma, theta):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.sigma = sigma
        self.theta = theta


    #This function calculates the utility for the consumer object the parameteres specified in the object
    #and the amount of consumed goods (Xhg) and factors provided (Vhf)
    #Xhg and Vhf are both one dimensional arrays with length of the number of goods / factors for this specific consumer
    
    def utilityFunction (self, Xhg, Vhf):

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
