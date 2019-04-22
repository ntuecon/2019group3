
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
            parameterDict : dictonary that contains all parameters that define the production function ()  """
        
        self.noProducer = noProducer
        self.noOfGoods = noOfGo
        self.noOfFactors = noOfFactors
        self.parameterDict = parameterDict

#constraint
        def prodtFct (r)
        """ This function calculates the production function """

        
         #seperate good array (Xhg) from factor array (Vhf) goods come first
        Xhg = numpy.array(inputList[0:self.noOfGoods])
        Vhf = numpy.array(inputList[self.noOfGoods: self.noOfGoods+ self.noOfFactors])
    


#objective
        def profitFct (Xhg, Vhg)
        """ In this section we define the profit function of producers"""
        

#maximization
        def maxProfit (r,p)

            """  This function maximizes the profit """
                    
       

