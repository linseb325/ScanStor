# Created by Brennan Linse on 10/3/17

# Responsible for setting up the simulation. Manages and responds appropriately to user prompts/input.

from Simulator import Simulator


class SimulatorManager:

    __simulator = None      # The simulator object which will process a list (array) using either SCAN or STOR.

    def beginSimulation(self):
        print("\n\nBEGINNING SIMULATION. We'll determine whether an array of integers contains repeating values.\n")
        print("First, we'll generate a list of random numbers.\n")

        inputLength = input("The length of the array will be... ?\n[Type an integer between 2 and 100, then press ENTER.]\n-> ")

        # Did the user type an int?
        try:
            inputLength = int(inputLength)
        except:
            print("\nInvalid input. Defaulting to length 10.")
            inputLength = 10

        # Is the user's input out of range?
        if inputLength > 100:
            print("\nToo high! Defaulting to length 100.")
        elif inputLength < 2:
            print("\nToo low! Defaulting to length 2.")


        inputMaxNum = input("\nThe numbers in the array will have values between 0 and... ?\n[Type an integer between 1 and 999, then press ENTER.]\n-> ")

        # Did the user type an int?
        try:
            inputMaxNum = int(inputMaxNum)
        except:
            print("\nInvalid input. Defaulting to max value 50.")
            inputMaxNum = 50

        # Is the user's input out of range?
        if inputMaxNum > 999:
            print("\nToo high! Defaulting to max value 999.")
        elif inputMaxNum < 1:
            print("\nToo low! Defaulting to max value 1.")

        self.__simulator = Simulator(inputLength, inputMaxNum)

        print("\nCreated the array. Here it is:\n")
        self.__simulator.displayArrayA()

        # Will we use SCAN or STOR?
        userChoice = input("\n\nNow, let's see if there's a matching pair in the list. Would you like to use SCAN or STOR?\n[Type 'scan' or 'stor', then press ENTER.]\n->").lower()

        if userChoice == "scan":
            result = self.__simulator.scan()
            if result == [-1, -1]:
                print("\nNO MATCHES!")
            else:
                print("\nFOUND A MATCH at indices " + str(result[0]) + " and " + str(result[1]) + ".")
        elif userChoice == "stor":
            result = self.__simulator.stor()
            if result == -1:
                print("\nNO MATCHES!")
            else:
                print("\nFOUND A MATCH: The value " + str(result) + " appears more than once in the list.")
        else:
            print("\nInvalid input. Defaulting to use SCAN.")
            result = self.__simulator.scan()
            if result == [-1, -1]:
                print("\nNO MATCHES!")
            else:
                print("\nFOUND A MATCH at indices " + str(result[0]) + " and " + str(result[1]) + ".")

        # Should we run another simulation?
        shouldRestartSim = input("\nWould you like to restart the simulation?\n[Type 'yes' if you'd like to restart, then press ENTER. If not, type anything else, then press ENTER.]\n->").lower()

        if shouldRestartSim == "yes":
            self.__simulator = None
            self.beginSimulation()
        else:
            print("\nOK. So long!")



