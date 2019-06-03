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
        print "The producer's profit function depends on the Elasticity of the product, that is xi or how easy is it to producer more of this product and Psi, the efficiency of that product " 
        print "The consumer has an utility function, that consists of the utility of the goods and the disutility of the factors provided"
        print "Alpha is the utility weight, and the alphas between different goods should add up to 1. Beta is the disutility weight of the factors provided"
        print "Sigma is the elasticity of substitution between goods."
        print "Gamma is the elasticity of consumption and Theta de elasticity of Factors. They are needed so the functions are well behaved and the Consumer doen't have unlimited wants."
 
    
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
            xi = float(raw_input ( "What do you want xi, the elasticity of the product, to be? Needs to be 0 and 1. We recommend 0.5, if you the input is closer to 0, then it becomes very elastic, and closer or above 1, it becomes very unelastic")
            psi = float(raw_input ( "What do you want psi, the technology or effiency of the product, to be? "))
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
                alpha = float(raw_input( "What do you want alpha, the weight of utility, to be? Must be greater than 0, unless this good is a bad and the alphas of different goods must add up to 1" ))
                alphaArray[j] = alpha
            beta = float(raw_input ( "What do you want beta, the weight of disutility, to be? Must be greater than 0, unless the consumer likes to give away this factor" ))
            gamma = float(raw_input ( "What do you want gamma,the elasticity of consumption, to be? Must be greater than 0 and less than 1. We recommend 0.5, if the chosen input is closer to 0, then it becomes very elastic, and closer or above 1, it becomes very unelastic"))
            sigma = float(raw_input ( "What do you want sigma, elasticity of substitution between goods, to be? Must be greater than 0, and LESS than 1. It's the elasticity between goods, if just one good, set it equal to 0" ))
            #If sigma is equal to 1, we could code a coub douglas function, it does not need gama and theta, because it is already well behaved.
            # It is ln (multiplier of xi to alphai), but we used the function of the sum of alpha i of ln (xi)
            thetaArray = numpy.empty(noOfFactors)
            for k in range (0, noOfFactors):
                theta = float(raw_input ( "What do you want theta, the elasticity of factors, to be? Must be greater than -1"))
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
        
        
