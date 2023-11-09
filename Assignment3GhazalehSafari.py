#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:57:45 2022

@author: Ghazaleh Safari

International Master- and PhD program in Mathematics
"""

""" Import modules"""
import numpy as np
import matplotlib.pyplot as plt

"""
Based on backgraund we have 10000 companies with the initial size = 10000.
So the frist x_t equals x_0.   
"""
num_comp = 10000
x_0 = 10000
x_t = x_0

"""
To plot the size of firms in t times (here we consider 500 frequencies as t),
we need a matrix with 10000 rows (as firms) and 500 colomns (as frequencies).
Therefore we consider kesten_matrix as an empty list firstly. By two "for 
loops" we compute the sizes of companies for t+1 times and save them in the
list called "kesten_matrix".
For that, in the first loop, we make an empty list called "list_sizes". Then 
by the second loop, we calculate the sizes of firms 500 times based on 
kesten process and add each one to the "list_sizes". 
"""
kesten_matrix = []

for comp_idx in range(10000):
    list_sizes = []
    for t in range(500):
        alpha_t = np.random.uniform(0.8, 1.2)
        beta_t = np.random.uniform(0, 10000)
        x_t1 = alpha_t * x_t + beta_t
        x_t = x_t1
        list_sizes.append(x_t1)
        
    kesten_matrix.append(list_sizes)
    
"""
To plot the results, we need change the list named "kesten_matrix" to a matrix
by numpy module. In the following prints, we can see the matrix and the size 
of that.
"""  
final_matrix = np.array(kesten_matrix)
print (final_matrix)
print(final_matrix.shape)

"""
By transposing the "final_matrix", we can show frequencies in ax_x and firms 
in ax_y
"""
final_matrix_transpose = final_matrix.transpose()



"""Now we plot the data and save the plot as a pdf file"""
plt.figure()
plt.plot(final_matrix_transpose)
plt.xlabel("frequency")
plt.ylabel("firms")
plt.savefig("kesten_function_distribution.pdf")


"""And we Plot the data in the semilog plot and save it as a pdf file"""
plt.figure()
plt.semilogx(final_matrix_transpose, color= "blue")
plt.xlabel("frequency")
plt.ylabel("firms")
plt.savefig("kesten_function_semi_log.pdf")


plt.show()

