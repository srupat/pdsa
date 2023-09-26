def factors(n):
    fl = []
    for i in range(1,n+1):
        if n%i==0:
            fl.append(i)
    return fl

def prime(n):
    return factors(n) == [0,1]

# for vs while
def primesupto(n):
    pl = []
    for i in range(1,n+1):
        if prime(i):
            pl.append(i)
    return pl

def firstprimes(m):
    (count, i , pl) = (0, 1, [])
    while(count<m):
        if prime(i):
            (count, pl) = (count + 1, pl + [i])
        i += 1
    return pl

# another method to check primality
def prime(n):
    result = True
    for i in range(2, n):
        if n%i == 0:
            result = False
    return result

# another way
def prime(n):
    result = True
    for i in range(2,n):
        if n%i == 0:
            result = False
            break
    return result

def prime(n):
    result, i = True , 2
    while (result and i<n):
        if (n%i==0):
            result = False
        i+=1
    return result

# optimized approach
import math
def prime(n):
    (result , i) = (True, 2)
    while(result and (i<math.sqrt(n))):
        if n%i==0:
            result = False
        i+=1
    return result

# twin primes if they have a diff of 2 
# dictionary concept

def primediff(n):
    lastprime = 2
    pd = dict()
    for i in range(3, n+1):
        if prime(i):
            d = i - lastprime
            lastprime = i
            if d in pd.keys():
                pd[d] = pd[d] + 1
            else:
                pd[d] = 1
    return pd

print(primediff(1000))