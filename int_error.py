import numpy as np

n = np.int16(0)
z = np.int32(2147483600)# I set this number here so it wouldn't take so long. It should work with this set to 0 but it takes a long time.
while np.int16(n+1) > 0:
    n = np.int16(n+1)

while np.int32(z+1) > 0:
    z = np.int32(z+1)
print('The largest number that can be represented in 16 bits is', n)
print('The largest number that can be represented in 32 bits is', z)
