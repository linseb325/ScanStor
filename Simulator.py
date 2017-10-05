# Created by Brennan Linse on 10/3/17

# Contains implementation of SCAN and STOR.

import random


class Simulator:

    __arrayA = []       # We look through this array for a pair of matching values.
    __arrayB = []       # Used to keep track of which values we've seen in STOR.
    __length = None     # The length of array A.
    __maxNum = None     # The maximum possible integer value for any element of array A.

    def __init__(self, listLength, maxElement):
        # We might need to change these below when we check whether the parameters are valid.
        self.__length = listLength
        self.__maxNum = maxElement

        # Check parameters
        if maxElement > 999:
            self.__maxNum = 999
        if maxElement < 1:
            self.__maxNum = 1

        if listLength < 2:
            self.__length = 2
        if listLength > 100:
            self.__length = 100

        # Fill array A with randomly generated numbers.
        self.__arrayA = []
        for x in range(0, self.__length):
            self.__arrayA.append(random.randrange(0, self.__maxNum+1))     # maxNum + 1 because randrange is exclusive for the 2nd argument




    # SCAN from NTO.
    # It's slower than STOR because we're effectively making two passes through array A (as evidenced by the nested loop structure).
    # This means we have to make more comparisons and execute more instructions than in STOR.
    def scan(self):
        for i in range(0, len(self.__arrayA)-1):
            for j in range(i+1, len(self.__arrayA)):
                if self.__arrayA[i] == self.__arrayA[j]:
                    return [i, j]

        return [-1, -1]     # This would mean we found no matches.


    # STOR from NTO.
    # It's faster than SCAN because we only have to make one pass through array A.
    # The trade-off is that STOR requires more memory to store array B.
    def stor(self):
        # First, fill array B with 0s. We need as many 0s as our maximum possible element number.
        self.__arrayB = []
        for x in range(0, self.__maxNum+1):
            self.__arrayB.append(0)

        for i in range(0, len(self.__arrayA)):
            if self.__arrayB[self.__arrayA[i]] == 1:
                return self.__arrayA[i]
            else:
                self.__arrayB[self.__arrayA[i]] = 1

        return -1       # This would mean we found no matches.




    # Print the array A to the console.
    def displayArrayA(self):
        print(self.__arrayA)

    # Print the array B to the console. (Didn't use it for this assignment. Might have been helpful for debugging, though.)
    def displayArrayB(self):
        print(self.__arrayB)



