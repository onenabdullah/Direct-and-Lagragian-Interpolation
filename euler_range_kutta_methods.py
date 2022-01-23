###         Euler Method            ### 


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
euler(xi,yi,xf,step)
heun(xi,yi,xf,step)
midpoint(xi,yi,xf,step)
ralston(xi,yi,xf,step)

a = euler(xi,yi,xf,step)
b = heun(xi,yi,xf,step)
c = midpoint(xi,yi,xf,step)
d = ralston(xi,yi,xf,step) 

# Comparing results
print("Comparing results below : ")
print("  Euler        Heun's        Midpoint        Ralston")
print("{:^9.4f}     {:^9.4f}      {:^9.4f}       {:^9.4f}" .format(a,b,c,d))