import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset here


# code for question 2
print('Problem 2 Answers:')
# code below this line
myfile = open('engagement_1.txt')
data = myfile.readlines()
myfile.close()

data = [float(x) for x in data]
sample_size = len(data)
sample_mean = np.mean(data)
s = np.std(data, ddof=1)
sample_se = s/m.sqrt(sample_size)
z_score = (sample_mean - 0.75)/sample_se
p_value = 2 * norm.cdf(-abs(z_score))
print('Sample size = ' + str(sample_size))
print('Sample mean = ' + str(sample_mean))
print('Standard error = ' + str(sample_se))
print('Standard score = ' + str(z_score))
print('p-value = ' + str(p_value))

# code for question 3
print('Problem 3 Answers:')
# code below this line
largest_se = abs((sample_mean - 0.75)/2)
min_sample_size = (s/largest_se)**2
print('Largest standard error = ' + str(largest_se))
print('Corresponding minimum smple size = ' + str(min_sample_size))

# code for question 5
print('Problem 5 Answers:')
# code below this line

myfile = open('engagement_0.txt')
data1 = myfile.readlines()
myfile.close()

data1 = [float(x) for x in data1]
sample_size1 = len(data1)
sample_mean1 = np.mean(data1)
s1 = np.std(data1, ddof=1)
se = m.sqrt((s**2)/sample_size + (s1**2)/sample_size1)
z = (sample_mean - sample_mean1)/se
p = 2 * norm.cdf(-abs(z))

print('Sample size = ' + str(sample_size1))
print('Sample mean = ' + str(sample_mean1))
print('Standard error = ' + str(se))
print('Standard score = ' + str(z))
print('p-value = ' + str(p))
