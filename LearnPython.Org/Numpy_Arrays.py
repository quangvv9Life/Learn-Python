# In the following example, you will first create two Python lists. 
# Then, you will import the numpy package and create numpy arrays out of the newly created lists.

height = [1.73, 1.7, 1.75, 1.5, 1.6]
weight = [73, 70, 77, 49, 83]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(type(np_height))

# Element-wise calculations : perform a calculation for each observation with a single equation
# These operations are very fast and computationally efficient
# For example, calculate the BMI for height & weight above : 

bmi = np_weight/ np_height ** 2

print(bmi)

# Another great feature of Numpy arrays is the ability to subset. 
# For instance, if you wanted to know which observations in our BMI array are above 23, we could quickly subset it to find out.


# Print only those observations above 23
print(bmi[bmi > 23])

# Example : 
# First, convert the list of weights from a list to a Numpy array. 
# Then, convert all of the weights from kilograms to pounds. 
# Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds.

weight_kg = [73, 70, 77, 49, 83]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg

np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs

print(np_weight_lbs)

