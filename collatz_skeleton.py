import numpy as np

def isEven(x):
    '''Checks an int to see whether it is even or not. Returns True
        if even, False if not'''
    if x%2 == 1:
        return False
    else:
        return True

def collatzCalc(number):
    '''Function that takes in a number and performs the collatz Calculation
        step. Returns an int.'''
    if isEven(number) is True:
        return int(number/2)
    else:
        return int(3*number+1)

def number_of_steps_to_one(number):
    """Function which determines how many steps
    it takes for a number to reach 1 in the Collatz
    sequence
    input: number (a positive integer)
    output: steps 
    """
    if not isinstance(number, int):
        raise ValueError("number must be integer")
    if not number>1:
        raise ValueError("number must be larger than one")
    newNumber = collatzCalc(number)
    steps = 1
    while newNumber != 1:
        newNumber = collatzCalc(newNumber)
        steps += 1
    return steps

if __name__ == "__main__":
    
    max_number_to_check = 10**5
    output = []
    
    for number in range(2, max_number_to_check+2):
        steps = number_of_steps_to_one(number)
        output.append((number, steps))
    #Writes output into a text file with two columns, one containing the number
    #and the second containing the number of steps it took to get to 1.
    file = open("collatzData.txt", "w")
    for i in range(len(output)):
        file.write(str(output[i][0]) + ' ' + str(output[i][1]) + '\n')
    file.close()
        
        
        
    #numbers_to_check = np.
    #Fill this section in 
    #write a for loop that iterates from 1 -> max_number to check
    #and calculates the number of steps to get to 1
