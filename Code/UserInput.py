"""
@author Michelle Pfister
@version 1.0

"""
import numpy

class UserInput (object):

    def __init__(self):
        pass
    
    def introduction (self):
        """ introduction will be used when beginning the economy simulation as a user to explain how the economy simuation work
        """
        print "Welcome to your Economy!"
        print "In the following you will be able to specify the parameters to your economy and be able to simulate your economy."
        print "But first a few explanations about this economy simulation. Your economy has three main actors: consumers, producers and the government. "
 
    
    def inputValues (self):
        """ inputValues will be used to describe to the user which parameters he has to input to define the economy (e.g. number of goods
        and factors, number of consumers and producers, link between consumer and producers). """
        
        #define number of goods and factors
        noOfGoods = int(raw_input("Please enter the number of goods of your economy : "))
        noOfFactors = int(raw_input("Please enter the number of factors of your economy : "))

        #define number of consumers and producers
        noOfConsumers = int(raw_input("How many consumers does your economy have? "))
        noOfProducers = int(raw_input ("How many producers does your economy have? "))


        #define for each producer what good they produce (to be discussed)
        parameterProd = [{}]*noOfProducers
        goodProd = numpy.empty(noOfProducers)
        for i in range(0,noOfProducers) :
            print "You define producer " + str(i+1) + " now"
            goodProducer = int(raw_input("Which product should this producer produce?"))
            xi = float(raw_input ( "What do you want xi to be?"))
            psi = float(raw_input ( "What do you want psi to be?"))
            producerDict = {"xi" : xi, "psi" : psi}
            goodProd[i] = goodProducer
            parameterProd[i] = producerDict
            


        #define for each consumer their shares of each producers profit (to be discussed)

        parameterCon = [{}]*noOfConsumers
        prodOfCon = numpy.empty(noOfConsumers)
        for i in range(0,noOfConsumers):
            print "You define consumer " + str(i+1) + " now"
            prodOfConsumer = int(raw_input("Which producers profit goes to this consumer?"))
            alphaArray = numpy.empty(noOfGoods)
            for j in range(0, noOfGoods):
                alpha = float(raw_input( "What do you want alpha to be?" ))
                alphaArray[j] = alpha
            beta = float(raw_input ( "What do you want beta to be?" ))
            gamma = float(raw_input ( "What do you want gamma to be?" ))
            sigma = float(raw_input ( "What do you want sigma to be?" ))
            thetaArray = numpy.empty(noOfFactors)
            for k in range (0, noOfFactors):
                theta = float(raw_input ( "What do you want theta to be? "))
                thetaArray[k] = theta

            consumerDict = {"alpha" : alphaArray, "beta" : beta, "gamma" : gamma, "sigma" : sigma, "theta" : thetaArray}
            parameterCon[i] = consumerDict
            prodOfCon[i] = prodOfConsumer

        value = Values(noOfGoods, noOfFactors, noOfConsumers, noOfProducers, parameterCon, parameterProd, prodOfCon, goodProd)

        return value

    
class Values(object):

    def __init__(self, noOfGoods, noOfFactors, noOfConsumers, noOfProducers, parameterCon, parameterProd, prodOfCon, goodProd ):
        self.prodOfCon = prodOfCon
        self.noOfGoods = noOfGoods
        self.noOfFactors = noOfFactors
        self.noOfConsumers = noOfConsumers
        self.noOfProducers = noOfProducers
        self.parameterCon = parameterCon
        self.parameterProd = parameterProd
        self.goodProd = goodProd
        
        
