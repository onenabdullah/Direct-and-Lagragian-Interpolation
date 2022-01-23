# Created  21 January 2022
# @author: AbdullahOnen



import numpy as np

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


