#!/usr/bin/python
# -∗- coding: utf-8 -∗-


def EstPair(n):
    if n%2==0:
        return True
    else:
        return False

def EstPremier(n):
     test=True
     for i in range(2,n//2+1):
         if n%i==0 and n!=2 :
             test=False
     return test


def f(x):
    return x**2-2
def dichotomie(f,a,b,epsilon=0.0001):
    assert ( a<b and f(a)*f(b) < 0) , "Il faut a<b et f(a)*f(b) < 0"
    while b-a > epsilon:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            a,b = a,c
        else:
            a,b = c,b
    return (a+b)/2


def Eratosthene(n):
    Liste_premier=[]
    L=[i for i in range(2,n+1)]
    while L!=[]:
        m=L[0]
        Liste_premier.append(m)
        M=[i  for i in L if i%m==0]
        for i in M:
            L.remove(i)
    return Liste_premier

def FacteurPremier(n):
    M=[]
    for i in Eratosthène(n):
        while n%i==0:
            M.append(i)
            n=n//i
    return M

