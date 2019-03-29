import numpy as np
from scipy.optimize import minimize 
import matplotlib as plt
from sympy import *

#We initialize 

#where Xg and Vg are the total numbers of goods and factors in the economy
class market_clearing (object):
  Xhg  = symbols('Xhg')
  Vhf = symbols('Vhf')
  Xg = symbols ('Xg')
  Vg = symbols ('Vg')


  def __init__(self,Xhg,Vhf,  Xg , Vg):
    self.Xhg = Xhg
    self.Vhf = Vhf
    self.Xg = Xg
    self.Vg = Vg
    
  #now we create the equilibrium method
  
  def obective1 (Xhg, Xg):
    return (Xhg - Xg) **2
  
  #now we make a guess
  
  X = [1,2]
  
  print (obective1 (X))
  
  sol = minimize (objective
    
