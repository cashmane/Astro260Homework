import matplotlib.pyplot as plt

def isEven(x):
    '''Takes in an int, and returns True if the int is even, False if it is odd'''
    number = x%2
    if number == 1:
        return False
    else:
        return True

def bindingCalc(A, Z):
    '''Function that uses the semi-empirical mass formula to return a value
        of the total nuclear binding energy of an atom. Takes in A (Mass Number)
        and Z (Atomic Number)'''
    t1 = (15.8 * A)
    t2 = (18.3*A**(2/3))
    t3 = (0.714*(Z**2))/(A**(1/3))
    t4 = 23.2*(((A-(2*Z))**2)/(A))
    if isEven(A) is False:
        a5 = 0
    elif isEven(Z) is True:
        a5 = 12.0
    else:
        a5 = -12.0    
    t5 = a5/(A**(1/2))
    answer = t1 - t2 - t3 - t4 + t5
    return answer

def bindingCalcPerNucleon(A, Z):
    '''Works just like bindingCalc function, but returns binding energy per
        nucleon instead of total binding energy. Inputs are A (Mass Number)
        and Z (Atomic Number)'''
    calc = bindingCalc(A, Z)
    calcPerNucleon = calc/A
    return calcPerNucleon

def singleValCalc(Z):
    '''Takes in a single value of Z (Atomic Number)and runs the binding Energy
        per Nucleon Calculation for all values of A from A = Z to A = 3Z, then
        returns the most stable value of A, along with the binding energy per
        nucleon for that configuration.'''
    end = 3*Z
    maxEnergy = None
    for i in range(Z, end):
        energy = bindingCalcPerNucleon(i, Z)
        if maxEnergy is None:
            answer = i
            maxEnergy = energy
        elif energy > maxEnergy:
            maxEnergy = energy
            answer = i
    return answer, maxEnergy

def findMostStable():
    '''Returns a list of the most stable configuration of each atom,
        from Z = 1 to Z = 100 (Z being the atomic number). The list contains a
        tuple with the most stable value of A (mass number) for each Z value,
        as well as the binding energy per nucleon for that atom.'''
    stableList = []
    for i in range(100):
        (aValue, energy) = (singleValCalc(i+1))
        stableList.append((aValue, energy))
    return stableList
        
        
        
        
        
        

A = 58 #Here is the input for Mass Number for the below calculations
Z = 28 #Here is the input for Atomic Number for the below calculations

print('The answer to part A is', bindingCalc(A, Z))
print('The answer to part B is', bindingCalcPerNucleon(A, Z))
print('The answer to part C is', singleValCalc(Z))
sList = findMostStable()
maxBindingEnergy = 0
zNumber = None
for i in range(100):
    print("For Z =", i+1, ", the most stable value of A is", sList[i][0])
    if sList[i][1] > maxBindingEnergy:
        maxBindingEnergy = sList[i][1]
        zNumber = i+1

print('The atom with the most binding energy per nucleon has','\n'
      'an atomic number of',zNumber,'with a binding energy of',
      maxBindingEnergy,'per nucleon')


f = open('nuclear_data.txt','r')
dataList = []
lines = f.readlines()
for line in lines:
    if line[0] == '#':
        continue
    else:
        dataList.append(line.split(' '))
f.close()


xValues = []
yValues = []
calcXValues = []
calcYValues = []
for i in range(len(dataList)):
    xValues.append(int(dataList[i][0]))
    yValues.append(float(dataList[i][5]))
    z = int(dataList[i][1])
    a = int(dataList[i][0])
    value = bindingCalcPerNucleon(a, z)
    calcXValues.append(a)
    calcYValues.append(value)
plt.figure(figsize=(15,10))
plt.plot(xValues, yValues, color = 'red', label ='Experimental Energy')
plt.scatter(calcXValues, calcYValues, color = 'blue', marker = '.', label='Calculated Energy')
plt.ylim((-5,10))
plt.ylabel('Binding Energy per Nucleon')
plt.xlabel('Mass Number')
plt.title('Experimental Values Vs. Calculations \n Binding Energy')
plt.legend()
plt.show()
    




        
    
