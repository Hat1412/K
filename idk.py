from math import sqrt
import matplotlib.pyplot as plt

def isprime(num):
    a=2
    while a <= sqrt(num):
        if num%a<1:
            return False
        
        a=a+1
    return num>1
    
def prime_series(n):
    l = [i for i in range(n) if isprime(i)]
    plt.scatter(l,[i for i in range(len(l))])

def Fib(n):
    l = [0,1]
    for _ in range(n - 2):
        c = l[-1] + l[-2]
        l.append(c)
        
    plt.scatter(l,[i for i in range(len(l))])

def AP(a,n,d):
    l = []
    for i in range(1,n + 1):
        l.append(a + (i-1) * d)

    plt.scatter(l,[i for i in range(len(l))])

    return l

def HS(l):
    res = []
    for i in l:
        res.append(round(1/i,2))

    return res

if __name__ == "__main__":
    plt.show()
