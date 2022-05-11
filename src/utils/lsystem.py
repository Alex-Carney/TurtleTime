# LSystem.py
"""
Created on Thu Feb  3 15:42:41 2022

@author: Gavin Burns (Framework by Alex)
"""
from collections import defaultdict
import numpy as np
from random import random


class LSystem:

    def __init__(self, alphabet, axiom, productions):
        """
        Parameters
        ----------
        alphabet : list[character, ... ]
            Set of characters to act upon. NOT USED
        axiom : character
            Starting character (or string)
        productions : List[[character, [string, string], [[string, float], ... ]], ... ]
            List of productions to be acted out in each iteration
            Written as [production1, production2, production3, ... ]
            Individual productions are written as ['parent', ['pre_context', 'post_context'], [['child1', 'child1_chance'], ['child2', 'child2_chance'], ... ]]
                Check production class for more details on production assembly

        Returns
        -------
        iteration_list : TYPE
            String after maxDepth+2 interations.

        """

        # initialize and declare instance variables
        self.alphabet = alphabet
        self.axiom = axiom
        self.productions = productions
        self.procedure_list = [None] * len(productions)  # emplt array of length equal to number of productions

        # when class is initialized
        # assemble list of productions into readable procedures
        for index, rule in enumerate(self.productions):
            self.procedure_list[index] = Production(rule[0], rule[1], rule[
                2])  # rule[1] is the parent(character),   rule[2] is the context[pre, post],   rule[3] is the list of potential children[['child1', 'child1_chance'],... ]]

    # recursive function for generating L-System Strings
    def l_string(self, maxDepth: int):

        self.iteration_list = [self.axiom]  # set the final string to the beggining axiom
        self.__next_l_string_helper(self.alphabet, self.axiom, self.procedure_list, maxDepth, 0,
                                    self.iteration_list)  # call __next_l_string_helper to continue recurssion

        # when full L-System has been generated return the final string
        return self.iteration_list[-1]

        # if you only want the full list of iterations of the L-System, use the following:
        # return self.iteration_list

    def __next_l_string_helper(self, alphabet, curr_string, procedure_list, maxDepth, currentDepth, iteration_list):
        # if we've reached max depth, exit recurssion loop
        if (currentDepth > maxDepth):
            return

        # prepare string to hold next iteration of L-System
        next_string = ""

        # print out the current L-System string (Just a sanity check)
        print(curr_string)

        # loop through each letter(value) of current L-System string
        for index, letter in enumerate(curr_string):
            # create a temporary string to hold a value to concatonate onto next_val
            # set the temp_value to the current letter (incase no valid procedure is found)
            temp_value = str(letter)

            # loop through each of the procedures
            for curr_procedure in self.procedure_list:
                parent = curr_procedure.parent

                # test to see if current letter of the L-System matches the parent letter of the current procedure
                if letter == parent:
                    # assign pre and post contexts of the current procedure
                    pre_context = curr_procedure.context[0]
                    post_context = curr_procedure.context[1]

                    # test to make sure the current L-System string contains the correct pre and post contexts of the current procedure
                    if (index >= len(pre_context)) and (
                            pre_context in curr_string[max(0, index - len(pre_context)): index]) and (
                            post_context in curr_string[(index + 1): index + 1 + len(post_context)]):
                        # generate a random number in the range [0.0, 1.0)
                        rand = random()

                        # get the correct bin for the generated number according to the bins in the current procedure
                        # check Prodcution class for explanation on bins
                        bin_num = np.digitize(rand, curr_procedure.bins)

                        # assign the temp_value to the correlated successor
                        temp_value = str(curr_procedure.name_dict[bin_num])

            # after looping through all procedures
            # concatonate the temp_value onto the next_string
            next_string += temp_value

        # after looping through the current L-System String
        # add the new strring to the list of L-System iterations
        iteration_list.append(str(next_string))

        # increment depth by one
        nextDepth = currentDepth + 1

        # call __next_l_string_helper again, with the next_string and nextDepth
        self.__next_l_string_helper(alphabet, next_string, procedure_list, maxDepth, nextDepth, iteration_list)

    # production string has the form [('predecessor', ['successor', probability]), ('predecessor', ['successor', probability]),]
    # def __init__(self, production_string):
    #    self.prod_dict = defaultdict(list)
    #
    #    for k,v in production_string:
    #        self.prod_dict[k].append(v)


class Production:
    # production list has the form [['ab', .5], ['ba', .5]]
    def __init__(self, parent, context, child_list):
        """
        Parameters
        ----------
        parent : character
            The predecessor of the entire production rule
        context : [string, string]
            The pre and post context necessary for a sucessor to be called
        child_list : List[[string, float], [string, float], ... ]
            A list of potential sucessor
            Each with a chance of occuring on the range of (0.0, 1.0]
            *IMPORTANT* The total of every child chance in a child list must not exceed 1.0; this will not work and will be the job of the user to recognize this

        Returns
        -------
        NONE

        """

        # initialize and declare instance variables
        self.parent = parent
        self.context = context
        self.child_list = child_list

        self.bins = np.array([1])  # bin sizes, list of partition locations for each bin
        self.bin_index = np.array([])  # bin labels/number, (int)
        self.name_list = np.array([])  # names associated with each bin

        # when intialized, immediately generate a procedure for the given variables
        self.generate_dict()

    def generate_dict(self):
        # for each child in the child_list
        for index, child in enumerate(self.child_list):
            child_name = child[0]  # name of successor (example: 'ab')
            child_chance = child[1]  # chance of successor being called

            # add a new bin
            self.bins = np.append(self.bins, (self.bins[
                                                  -1] - child_chance))  # when new bins are added, we will subtract the current child_chance from the previous partition
            self.bin_index = np.append(self.bin_index,
                                       (index + 1))  # number the new bin by incrementing the previous bin's label by 1
            self.name_list = np.append(self.name_list,
                                       child_name)  # associate the current bin to the current child name

        # if the last bin is above or below 0
        if self.bins[-1] != 0:
            # create a new bin and set it to 0
            self.bins = np.append(self.bins, 0)
            self.bin_index = np.append(self.bin_index, self.bin_index[-1] + 1)
            self.name_list = np.append(self.name_list, self.parent)

        # create a dictionary from the bin labels to
        self.bin_to_name = zip(self.bin_index, self.name_list)
        self.name_dict = dict(self.bin_to_name)

        # Print out the procedure (Sanity Check)
        print(self.context[0], "<", self.parent, ">", self.context[1], " -> ", self.name_dict)


# Main method for testting the system
def main():
    # Reminder!! the "Productions" parameter for the L-System Class is writtten as follows:
    # [production1, production2, production3, ... ]

    # The produciton variable should be formated as follows:
    # ['parent', ['precontext', postcontext'], [child_list]]

    # Lastly, the child_list is formated as follows:
    # [['child1', child1_chance], ['child2', child2_chance], ['child3', child3_chance], ...]

    # Here is a simple example
    child1 = ['A', 0.25]
    child2 = ['G', 0.5]
    child3 = ['V', 0.25]

    child_list = [child1, child2, child3]

    production = ['J', ['', ''], child_list]

    math_comp = LSystem(['J', 'A', 'G', 'V'], 'Jeremy', [production])
    math_comp_str = math_comp.l_string(0)
    print(math_comp_str)
    print()
    print()

    ####################Some More Detailed Examples##################################################################################################################################################

    # General Testbenching
    productions = [['a', ['', 'c'], [['ab', 0.5], ['ba', 0.5]]], ['a', ['', 'b'], [['ac', 0.5]]],
                   ['a', ['b', ''], [['ca', 1.0]]], ['b', ['', ''], [['c', 1.0]]], ['c', ['', ''], [['b', 1.0]]]]
    system = LSystem(['a', 'b', 'c'], 'ab', productions)
    system_str = system.l_string(7)
    print(system_str)
    print()
    print()

    #    #Fibonacci Example
    #    fibonacci_productions = [['a', ['', ''], [['b', 1.0]]], ['b', ['', ''], [['ab', 1.0]]]]
    #    fib_system = LSystem(['a', 'b', 'c'], 'ab', fibonacci_productions)
    #    fib_system_str = fib_system.l_string(4)
    #    print(fib_system_str)
    #    print()
    #    print()

    # Koch Turtle Example
    #    koch_productions = [['F', ['', ''], [['F-F+F+FF-F-F+F', 1.0]]]]
    #    koch_system = LSystem(['F', '-', '+'], 'F', koch_productions)
    #    koch_system_str = koch_system.l_string(1)
    #    print(koch_system_str)
    #    print()
    #    print()

    # Stochastic Testing
    sto_productions = [['a', ['', ''], [['ab', 0.5], ['ba', 0.3], ['a', 0.2]]],
                       ['b', ['', ''], [['c', 0.1], ['b', 0.5], ['d', 0.4]]],
                       ['c', ['', ''], [['cd', 0.3], ['d', 0.33333333]]],
                       ['d', ['', ''], [['a', 0.12325423], ['ab', 0.5423]]]]
    stochastic_system = LSystem(['a', 'b', 'c', 'd'], 'abcd', sto_productions)
    stochastic_system_str = stochastic_system.l_string(7)
    print(stochastic_system_str)
    print()
    print()

    # Context Dependent Testing
    productions = [['a', ['', 'b'], [['ca', 1.0]]], ['a', ['b', ''], [['ac', 1.0]]], ['b', ['a', 'a'], [['bbb', 1.0]]],
                   ['b', ['b', 'b'], [['a', 1.0]]]]
    system = LSystem(['a', 'b', 'c'], 'aba', productions)
    system_str = system.l_string(7)
    print(system_str)
    print()
    print()


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