"""
@author Michelle Pfister
@version 1.0

"""

class UserInput (object):

    def __init__(self, noOfGoods, noOfFactors, noOfConsumers, noOfProducers):
        self.noOfGoods = noOfGoods
        self.noOfFactors = noOfFactors
        self.noOfConsumer = noOfConsumers
        self.noOfProducer = noOfProducers
    
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
        noOfGoods = raw_input("Please enter the number of goods of your economy : ")
        noOfFactors = raw_input("Please enter the number of factors of your economy : ")

        #define number of consumers and producers
        noOfConsumers = raw_input("How many consumers does your economy have? ")
        noOfProducer = raw_input ("How many producers does your economy have? ")

        #define for each producer what good they produce (to be discussed)


        #define for each consumer their shares of each producers profit (to be discussed)
        
        
        #what else do we need to determine the economy?
        
        
    
        
  

