"""
@author Michelle Pfister
@version 1.0

"""

import numpy
from Consumer import Consumer
from Producer import Producer
from UserInput import UserInput
#from Economy import Economy

    
#explanation
user = UserInput()
user.introduction()

#input of data by the user has to happen using functions of the class UserInput
value = user.inputValues()
    
#consumer objects will be created

consumerArray = [Consumer]*value.noOfConsumers
for c in range(0,len(consumerArray)):
    consumerArray[c] = Consumer(value.prodOfCon[c],value.noOfGoods,value.noOfFactors,value.parameterCon[c])
    #NOOFPRODUCER HAS TO BE CHANGED

print "Consumer created"
    
#producer objects will be created
producerArray = [Producer]*value.noOfProducers
for p in range(0,len(producerArray)):
    producerArray[p] = Producer(value.noOfProducers, value.noOfGoods, value.noOfFactors, value.parameterProd[p], value.goodProd[p])

print "Producer created"
    

#economy object will be created (giving the object information on number

#economy = Economy ( #HAS TO BE CREATE 
#goods and factors, arrays of the created consumers and producers

#findEquilibrium() method will be called to let the equilibrium be calculated

