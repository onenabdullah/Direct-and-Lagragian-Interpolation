#author : AbdullahOnen

import numpy as np

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
    print ("%.3fx**%s"%(a_values[i],i), end=(" "))
    
print("\n")

print('\nInterpolated result by direct method at %.3f is %s' % (searchingvalue, lag_result))


print("\nInterpolated result by lagrangian method at %.3f is %s" %(searchingvalue,dm_result))


