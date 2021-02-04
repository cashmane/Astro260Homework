import numpy as np

def bad_float_compare(a, b):
    if a == b:
        return True
    else:
        return False
    
def good_float_compare(a, b):
    epsilon = 1e-10
    if abs(a-b) < epsilon:
        return True
    else:
        return False
    

a = 1e20
b = 1e-7

print('A + B - A is', a+b-a)
print('A is', a)
print('B is', b)

float1 = 50000893.57839878
float2 = 50000893.57839877

assert bad_float_compare(float1, float2) is False
assert good_float_compare(float1, float2) is False

print(float1 - float2)

