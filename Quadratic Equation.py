#Program to calculate the quadratic equation using function returning multiple values

import cmath

def quadEquation(a,b,c):
    x1 = (-b + cmath.sqrt( b**2 -4 * a * c))/(2 * a) 
    x2 = (-b - cmath.sqrt( b**2 -4 * a * c))/(2 * a) 

    return x1,x2

if __name__ == "__main__" :
    print("Program to calculate quadratic equation.")
    a = int(input("Enter the value of a = "))
    b = int(input("Enter the value of b = "))
    c = int(input("Enter the value of c = "))

    x1,x2 = quadEquation(a,b,c)
    print(x1,x2)
