# LSystem.py
"""
Created on Thu Feb  3 15:42:41 2022

@author: Alex Carney
"""
from collections import defaultdict
import numpy as np

class LSystem:
    def __init__(self, alphabet, axiom, procedure_dictionary):
        """
        Parameters
        ----------
        alphabet : list[characters]
            Set of characters to act upon
        axiom : character
            Starting character (or string)
        procedure_dictionary : List of key/value procedure rules
            List of procedures, written in a key:value format. 

        Returns
        -------
        final_string : TYPE
            String after maxDepth+2 interations.

        """
        self.alphabet = alphabet
        self.axiom = axiom
        self.procedure_dictionary = procedure_dictionary
        
        #procedure_dictionary is a list of lambdas 
    def l_string(self, maxDepth: int):
            
        self.final_string = [self.axiom]
        self.__next_l_string_helper(self.alphabet, self.axiom, self.procedure_dictionary, maxDepth, 0, self.final_string)
            
            
        return self.final_string
        
    def __next_l_string_helper(self, alphabet, current_val, procedure_dictionary, maxDepth, currentDepth, final_string):
        if(currentDepth > maxDepth):
            return
        next_val = ""
        for value in current_val:
            next_val += str(procedure_dictionary[value]) 
        final_string.append(str(next_val))
           
        nextDepth = currentDepth + 1
        self.__next_l_string_helper(alphabet, next_val, procedure_dictionary, maxDepth, nextDepth, final_string)
    
    
    #production string has the form [('predecessor', ['successor', probability]), ('predecessor', ['successor', probability]),]
    #def __init__(self, production_string):
    #    self.prod_dict = defaultdict(list)
    #    
    #    for k,v in production_string:
    #        self.prod_dict[k].append(v)

class Production:
    
    #production list has the form [['ab', .5], ['ba', .5]]
    def __init__(self, predecessor, successor_list):
        self.bins = np.array([1])
        self.highMark = 1
        self.bin_idx_to_succ = {}
        
        for i, possible_succ in enumerate(successor_list):
            print(i)
            
            #add a new entry to the bins -> 1 , 1-prob1, prob1-prob2, etc.
            new_bin_high_value = self.highMark - possible_succ[1]
            #self.bins.append(newBinHighValue)
            self.bins = np.append(self.bins, new_bin_high_value)
            self.highMark = new_bin_high_value
    
            
        
        
        

        
        

def main(): 
    #Test Production
    #productions = [('a', ['ab', .5]), ('a', ['ba', .5]), ('b', ['a', 1])]
    succ_list = [['ab', 0.5], ['ba', 0.5]]
    prod = Production('a', succ_list)
    print(prod.bins)
    print(prod.highMark)
    
    x = .999999
    indx = np.digitize(x, prod.bins)
    print(indx)
    
    
    
    #Fibonacci Example
    fibonacci_dictionary = {'a': 'ab', 'b': 'a'}
    fib_system = LSystem(['a','b'], 'b', fibonacci_dictionary)
    fib_system_str = fib_system.l_string(6)
    print(fib_system_str)
    
    #Koch Turtle Example
    koch_turtle_dictionary = {'F': 'F-F+F+FF-F-F+F', '-': '-', '+': '+'}
    koch_system = LSystem(['F', '-', '+'], 'F-F-F-F', koch_turtle_dictionary)
    koch_system_str = koch_system.l_string(0)
    print(koch_system_str)
    
    
    
    
    
    
    
# =============================================================================
#     bruhMoment = l_string(['0', '1'], 'b', fibonacci_dictionary, 6)
#     
#     thue_morese_dictionary = {'0': '01', '1': '10'}
#     bruhMoment2 = l_string(['0', '1'], '0', thue_morese_dictionary, 4)
#     
#     cantor_ternary_dictionary = {'A': 'ABA', 'B': 'BBB'}
#     bruhMoment3 = l_string(23, 'A', cantor_ternary_dictionary, 2)
#     
#     koch_turtle_dictionary = {'F': 'F-F+F+FF-F-F+F', '-': '-', '+': '+'}
#     bruhMoment4 = l_string(23, 'F-F-F-F', koch_turtle_dictionary, 1)
#     
#     hilbert_curve_dictionary = {'A': '+BF-AFA-FB+', 'B': '-AF+BFB+FA-', 'F':'F','+':'+','-':'-' }
#     bruhMoment5 = l_string(23, 'A', hilbert_curve_dictionary, 1)
# =============================================================================
    
    
    
# =============================================================================
#     print(bruhMoment)
#     print(bruhMoment2)
#     print(bruhMoment3)
#     print(bruhMoment4)
#     print(bruhMoment5)
# =============================================================================
    

#Defining a main method and calling it like this is required for any module that will be imported into other modules. 
if __name__ == '__main__':
    main()
    
    
    

        
        
    
    
    
