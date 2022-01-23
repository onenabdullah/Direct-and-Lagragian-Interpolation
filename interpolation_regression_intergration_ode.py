# author : AbdullahOnen      
# January 2022

import numpy as np
import sympy as sy

### Firstly selecting process type

process_type = int(input("1 for Interpolation\n2 for Regression\n3 for Integration\n4 for Ordinary Differential Equaiton\nPlease select the process you want to do : "))

if process_type==1:
    degree_of_polynomial= int(input("Please enter the degree of polynomial : "))
    data_points = int(input("Please enter the number of data points (You must enter one more data point than the degree of the polynomial.) : "))
    x_points = np.zeros((data_points))
    y_points = np.zeros((data_points))
    our_matrix = np.ones((data_points,degree_of_polynomial+1))

    # Getting values #

    print('Enter data for x and y: ')

    for i in range(data_points):
        x_points[i] = float(input( 'x['+str(i)+']='))
        y_points[i] = float(input( 'y['+str(i)+']='))

    searchingvalue = float(input("Please enter the value you want to find : "))

    #### Direct Method of Interpolation ####

    # Creating a matrix of unknowns # 
    
    for i in range(data_points):
        for j in range(1,degree_of_polynomial+1):
            our_matrix[i][j] = (x_points[i])**(j)

    # Finding the unknowns #

    a_values = np.linalg.solve(our_matrix,y_points)

    dm_result = 0
    for i in range(len(a_values)):
        dm_result += a_values[i]*(searchingvalue**i)
    
    
        #### Lagrangian Interpolation ####

    # f(x) = Sum(L(x))f(xi) 
    # Li(x) = multiply((x-xj)/xi-xj)), let's apply rule
    
    lag_result = 0      #create result value firstly ineffectively

    for i in range(data_points):
        
        L_value = 1     #create L value firstly ineffectively
    
        for j in range(data_points):
            if i != j:
                L_value = L_value * (searchingvalue  - x_points[j])/(x_points[i] - x_points[j])
    
        lag_result = lag_result + L_value * y_points[i]    
    
    ## Results 
    print("\nInterpolated function is",end=(" "))
    for i in range(len(a_values)):
        print ("%.3fx**%s"%(a_values[i],i), end=("+"))
    
    print("\n")

    print('\nInterpolated result by direct method at %.5f is %s' % (searchingvalue, lag_result))

    print("\nInterpolated result by lagrangian method at %.5f is %s" %(searchingvalue,dm_result))
    
if process_type==2:
    func_type = int(input("1 for linear y=a+bx\n2 for non_linear and y = a*(x**b)\n3 for non_linear and y = a*(b**(x)) \nPlease select the your function type : "))
    ######          REGRESSION            ######         
    
    # f(x) = a0+a1*x
    # a1 = (n*sum(xi*yi)*sum(xi)*sum(yi))/(n*(sumxi**2)-(sumxi)**2), lets apply
    
    # Getting values #
    data_points = int(input("Please enter the number of data points : "))
    x_points = np.zeros((data_points))
    y_points = np.zeros((data_points))

    print("Enter data:")
    for i in range(data_points):
        x_points[i] = float(input( 'x['+str(i)+']='))
        y_points[i] = float(input( 'y['+str(i)+']='))



    # crete sum values ineffectively then applying least square method

    sumX = 0            # sum of x values
    sumX2 = 0           # sum of x**2 values
    sumY = 0            # sum of y values
    sumXY = 0           # sum of x*y values

    ####            Linear Regression       ####
    if func_type == 1:
        for i in range(data_points):
            sumX = sumX + x_points[i]
            sumX2 = sumX2 + x_points[i]*x_points[i]
            sumY = sumY + y_points[i]
            sumXY = sumXY + x_points[i]*y_points[i]

    # applying formula

        b = (data_points*sumXY-sumX*sumY)/(data_points*sumX2-sumX*sumX)
        a = (sumY/data_points)-(b*sumX)/data_points
        print("Our equation is: y = %0.4f + %0.4fx" %(a,b))
    ####            Non_Linear Regression       ####

    ###         y = a*(x**b)                    ###
    if func_type == 2:
        for i in range(data_points):
            sumX = sumX + np.log(x_points[i])
            sumX2 = sumX2 +np.log(x_points[i])*np.log(x_points[i])
            sumY = sumY + np.log(y_points[i])
            sumXY = sumXY + np.log(x_points[i])*np.log(y_points[i])

        # applying formula

        b = (data_points*sumXY-sumX*sumY)/(data_points*sumX2-sumX*sumX)
        ln_a = (sumY/data_points)-(b*sumX)/data_points


        # Obtaining a and b
        a = np.exp(ln_a)
    
        print("Our equation is: y = %0.4f * x**%0.4f" %(a,b))
    
    ###             y = a*(b**(x))               ### 
    if func_type == 3:
        for i in range(data_points):
            sumX = sumX + x_points[i]
            sumX2 = sumX2 +x_points[i]*x_points[i]
            sumY = sumY + np.log(y_points[i])
            sumXY = sumXY + x_points[i]*np.log(y_points[i])
            
            # Finding coefficients ln_a and ln_b
            ln_b = (data_points*sumXY-sumX*sumY)/(data_points*sumX2-sumX*sumX)
            ln_a = (sumY/data_points)-(ln_b*sumX)/data_points

        # Obtaining a and b
        a = np.exp(ln_a)
        b = np.exp(ln_b)
        print("Our equation is: y = %0.4f *%0.4f**x" %(a,b))
    #Results
    
    print("\n Coefficients of our functions are :")
    print("a : %.4f "%(a))
    print("b : %.4f" %(b))
    
    

if process_type == 3:
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
    

if process_type==4:
    ###         Euler Method            ### 
    print("\n Calculations are made according to the function in the code , if you want to calculate another function, please change the code\nOur equaiton is -2.2067*(10**(-12))*((y**4) - 81*(10**8))\n")
    
    # Getting values
    print('Please enter initial points:')
    xi = float(input('xi = '))
    yi = float(input('yi = '))

    print('Please enter the point you want to find : ')
    xf = float(input('xf = '))

    print('Please enter how many steps you want to do the process :')
    step = int(input('Number of steps = '))



    # Defining our function (If you want calculate your function, enter your function below line )
    def f(x,y):
        return -2.2067*(10**(-12))*((y**4) - 81*(10**8))


    # Euler method's function

    # y1 = y0 + f(x0,y0)*(x1-x0), so let apply rule

    def euler(xi,yi,xf,n):
        
        # Number of steps
        
        h = (xf-xi)/n
        
        # Some print jobs to make it look better and applying method
        print("\nEuler method's solution : ")
        print('\nstep        xi value        yi value        slope        result')    
        
        for i in range(n):
            slope = f(xi,yi)
            yf = yi + h * slope    #new y value
            print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(i,xi,yi,slope,yf))
            
            yi = yf             #prepare next step
            xi = xi+h           #prepare next step
        
        print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(n,xi,yi,slope,yf))
        return yf

    ###         Heun's Method            ### 

    # Heun's method's function

    # a1 = 1/2
    # a2 = 1/2
    # p1 = 1
    # q11 = 1 so;
    # k1 = f(x0,y0)
    # k2 = f(xi+h,yi+k1*h) finally;

    # y1 = y0 + (0.5*k1+0.5*k2)*h, so let apply rule


    def heun(xi,yi,xf,n):
        
        # Number of steps
        h = (xf-xi)/n
        
        # Some print jobs to make it look better and applying method
        print("\nHeun's method's solution : ")
        print('\nstep        xi value        yi value        slope        result')    

        for i in range(n):
            slope = f(xi,yi)
            k1 = slope
            k2 = f(xi+h,yi+k1*h)
            
            yf = yi + (0.5*k1 + 0.5*k2)*h
            print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(i,xi,yi,slope,yf))
            
            yi = yf
            xi = xi+h
        
        print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(n,xi,yi,slope,yf))
        return yf

    # Midpoint method's function

    # a1 = 0
    # a2 = 1
    # p1 = 1/2
    # q11 = 1/2 so;
    # k1 = f(x0,y0)
    # k2 = f(xi+0.5*h,yi+0.5*k1*h) finally;

    # y1 = y0 + k2*h, so let apply rule

    def midpoint(xi,yi,xf,n):
        
        # Number of steps
        h = (xf-xi)/n
        
        # Some print jobs to make it look better and applying method
        print("\nMidpoint method's solution : ")
        print('\nstep        xi value        yi value        slope        result')    

        for i in range(n):
            slope = f(xi,yi)
            k1 = slope
            k2 = f(xi+0.5*h,yi+0.5*k1*h)
            
            yf = yi + (0*k1 + 1*k2)*h
            print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(i,xi,yi,slope,yf))
            
            yi = yf
            xi = xi+h
        
        print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(n,xi,yi,slope,yf))
        return yf


    # a1 = 1/3
    # a2 = 2/3
    # p1 = 3/4
    # q11 = 3/4 so;
    # k1 = f(x0,y0)
    # k2 = f(xi+0.75*h,yi+0.75*k1*h) finally;

    # y1 = y0 + (1/3*k1+2/3*k2)*h, so let apply rule

    def ralston(xi,yi,xf,n):
        
        # Number of steps
        h = (xf-xi)/n
        
        # Some print jobs to make it look better and applying method
        print("\nRalston method's solution : \n")   
        print('step        xi value        yi value        slope        result')    

        for i in range(n):
            slope = f(xi,yi)
            k1 = slope
            k2 = f(xi+0.75*h,yi+0.75*k1*h)
            
            yf = yi + ((1/3)*k1 + (2/3)*k2)*h
            print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(i,xi,yi,slope,yf))
            
            yi = yf
            xi = xi+h
        
        print("{:^4}      {:^8.4f}       {:^10.4f}      {:^7.4f}      {:^7.4f}" .format(n,xi,yi,slope,yf))
        return yf


    # Anddd result 

    a = euler(xi,yi,xf,step)
    b = heun(xi,yi,xf,step)
    c = midpoint(xi,yi,xf,step)
    d = ralston(xi,yi,xf,step) 

    # Comparing results
    print("\nComparing results below : \n")
    print("  Euler        Heun's        Midpoint        Ralston")
    print("{:^9.4f}     {:^9.4f}      {:^9.4f}       {:^9.4f}" .format(a,b,c,d))
    