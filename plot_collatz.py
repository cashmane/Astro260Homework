import matplotlib.pyplot as plt
import numpy as np

def plotDataInRange(data, n):
    '''Takes in the data as numpy array, and plots the data in the range
        from 1 to n. '''
    xList = []
    yList = []
    for i in range(n):
        xList.append(data[i][0])
        yList.append(data[i][1])
    plt.xlabel('Number')
    plt.ylabel('Number of Steps')
    plt.plot(xList, yList)
    plt.title('Collatz Conjecture')
    plt.show()
        

if __name__ == "__main__":
    inputfile = 'collatzData.txt'
    data = np.genfromtxt(open('collatzData.txt'), dtype=np.int, 
                         skip_header=0)
    n = 100 #Change this number to change the range of the graph.. up to 100000  
    plotDataInRange(data, n)
    
