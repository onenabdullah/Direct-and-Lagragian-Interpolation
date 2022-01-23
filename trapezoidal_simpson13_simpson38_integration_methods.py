# Created  22 January 2022
# @author: AbdullahOnen

import sympy as sy


# Defining our function (If you want calculate your function, enter your function below line )
print("Calculations are made according to the function in the code , if you want to calculate another function, please change the code\nOur function is 1/x**2")
def f(x):
    return 1/x**2

#Trapezoidal rule's function

# f1(x) = f(a)+(f(b)-f(a))/(b-a) * (x-a), let's apply rule

def trapezoidal(xi,xf,n):
    # calculation steps
    h = (xf - xi) / n
    
    # Summation
    integ = f(xi) + f(xf)
    
    for i in range(1,n):
        k = xi + i*h
        integ = integ + 2 * f(k)
    
    # Finding final integration value
    integ = integ * h/2
    
    return integ


#Simpson's 1/3 rule's function

def simpson13(xi,xf,n):
    # calculating step size
    h = (xf - xi) / n
    
    # Summation
    integ = f(xi) + f(xf)
    
    for i in range(1,n):
        k = xi + i*h
        
        if i%2 == 0:
            integ = integ + 2 * f(k)
        else:
            integ = integ + 4 * f(k)
    
    # Finding final integration value
    integ = integ * h/3
    
    return integ


#Simpson's 3/8 rule's function

def simpson38(xi,xf,n):
    # calculating step size
    h = (xf - xi) / n
    
    # Finding sum 
    integ = f(xi) + f(xf)
    
    for i in range(1,n):
        k = xi + i*h
        
        if i%2 == 0:
            integ = integ + 2 * f(k)
        else:
            integ = integ + 3 * f(k)
    
    # Finding final integration value
    integ = integ * 3 * h / 8
    
    return integ
    


# Giving values
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))


# Finding values

result_trap = trapezoidal(lower_limit,upper_limit, sub_interval)
result_simpson13 = simpson13(lower_limit,upper_limit, sub_interval)
result_simpson38 = simpson38(lower_limit,upper_limit, sub_interval)

# Exact value of integral 
x = sy.Symbol("x")
exact_value = sy.integrate(f(x), (x, lower_limit, upper_limit))

#Relative approximation error of each methods 

Et_trap = abs(exact_value-result_trap)/exact_value

Et_simpson13 = abs(exact_value-result_simpson13)/exact_value

Et_simpson38 = abs(exact_value-result_simpson38)/exact_value

#Output of values and comparing 

print("\n\nExact value of integral %8.6f \n\nResults are methods and their relative aprroximation are : \n" %(exact_value))

print("                     No of interval        Result          Et        ")

print("Trapezoidal   method {:^14}       {:^8.6f}       {:^7.5f}".format(sub_interval,result_trap,Et_trap),"%")

print("Simpson's 1/3 method {:^14}       {:^8.6f}       {:^7.5f}".format(sub_interval,result_simpson13,Et_simpson13),"%")

print("Simpson's 3/8 method {:^14}       {:^8.6f}       {:^7.5f}".format(sub_interval,result_simpson38,Et_simpson38),"%")

