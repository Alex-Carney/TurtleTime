# LSystem.py
"""
Created on Thu Feb  3 15:42:41 2022

@author: Gavin Burns
"""
from collections import defaultdict
import numpy as np
from random import random


class LSystem:

    def __init__(self, alphabet, axiom, procedure_dictionary, context=False):
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
        self.context = context

    def generate_dict(self, key_value, rules):
        self.key_value = key_value
        # procedure_dictionary is a list of lambdas
    def l_string(self, maxDepth: int):

        self.final_string = [self.axiom]
        self.__next_l_string_helper(self.alphabet, self.axiom, self.procedure_dictionary, maxDepth, 0,
                                    self.final_string)

        return self.final_string

    def __next_l_string_helper(self, alphabet, current_val, procedure_dictionary, maxDepth, currentDepth, final_string):
        if (currentDepth > maxDepth):
            return
        next_val = ""
        for value in current_val:
            next_val += str(procedure_dictionary[value])
        final_string.append(str(next_val))

        nextDepth = currentDepth + 1
        self.__next_l_string_helper(alphabet, next_val, procedure_dictionary, maxDepth, nextDepth, final_string)

    # production string has the form [('predecessor', ['successor', probability]), ('predecessor', ['successor', probability]),]
    # def __init__(self, production_string):
    #    self.prod_dict = defaultdict(list)
    #
    #    for k,v in production_string:
    #        self.prod_dict[k].append(v)


class Production:

    # production list has the form [['ab', .5], ['ba', .5]]
    def __init__(self, parent, child_list):
        # some initializing junk
        self.bins = np.array([1])
        self.bin_index = np.array([])
        self.name_list = np.array([])
        #        self.high_mark = 1 #NIU_1

        for index, child in enumerate(child_list):
            # check current index and child
            #            print() #NIU
            #            print(index, child) #NIU

            child_name = child[0]  # possible successor (example: 'ab')
            child_chance = child[1]  # chance of successor

            # reduce the high mark by chance of the new successor
            #            new_high_mark = self.high_mark - child_chance #NIU_1
            #            self.high_mark = new_high_mark #NIU_1

            # add a new entry to the bins -> 1 -> 1-prob1 -> 1-prob1-prob2, etc.
            # each bin is the range in between each high_mark
            self.bins = np.append(self.bins, (self.bins[-1] - child_chance))
            self.bin_index = np.append(self.bin_index, (index + 1))
            self.name_list = np.append(self.name_list, child_name)

            # check current values
        #            print(self.bins) #NIU
        #            print(self.bin_index) #NIU
        #            print(self.name_list) #NIU

        self.bin_to_name = zip(self.bin_index, self.name_list)
        self.name_dict = dict(self.bin_to_name)

        print(self.name_dict)


def main():
    # Test Production
    # productions = [('a', ['ab', .5]), ('a', ['ba', .5])]
    succ_list = [['ab', 0.5], ['ba', 0.2], ['bb', 0.3]]
    prod = Production('a', succ_list)
    print(prod.bins)

    x = random()
    index = np.digitize(x, prod.bins)

    print()
    print(x)
    print(prod.name_dict[index])

    # Fibonacci Example


#    fibonacci_dictionary = {'a': 'ab', 'b': 'a'}
#    fib_system = LSystem(['a','b'], 'b', fibonacci_dictionary)
#    fib_system_str = fib_system.l_string(6)
# print(fib_system_str)

# Koch Turtle Example
#    koch_turtle_dictionary = {'F': 'F-F+F+FF-F-F+F', '-': '-', '+': '+'}
#    koch_system = LSystem(['F', '-', '+'], 'F-F-F-F', koch_turtle_dictionary)
#    koch_system_str = koch_system.l_string(0)
# print(koch_system_str)


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


# Defining a main method and calling it like this is required for any module that will be imported into other modules.
if __name__ == '__main__':
    main()









