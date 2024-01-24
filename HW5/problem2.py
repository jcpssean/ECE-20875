import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]

# code for question 1
print('Problem 1 Answers:')
# code below this line
n = len(data)
df = n-1
p = (1 - 0.90) / 2
mean = np.mean(data)
s = m.sqrt(1/(n-1)*sum((data-mean)**2))
se = s/m.sqrt(n)
tc = stats.t.ppf(1 - p, df)
lb = mean - tc * se
ub = mean + tc * se
print('mean = ' + str(mean))
print('s = ' + str(s))
print('standard error = ' + str(se))
print('tc = ' + str(tc))
print('interval = ({}, {})'.format(lb, ub))

# code for question 2
print('Problem 2 Answers:')
# code below this line
p2 = (1 - 0.95) / 2
tc2 = stats.t.ppf(1 - p2, df)
lb2 = mean - tc2 * se
ub2 = mean + tc2 * se
wide = False
if (ub2 > ub) and (lb2 < lb):
    wide = True
print('t-value = ' + str(tc2))
print('interval = ({}, {})'.format(lb2, ub2))
print(wide)

# code for question 3
print('Problem 3 Answers:')
# code below this line
s3 = 15.836
se3 = s3/m.sqrt(n)
zc = stats.norm.ppf(1-p2)
lb3 = mean - zc * se3
ub3 = mean + zc * se3
wide2 = False
if (ub3 > ub2) and (lb3 < lb2):
    wide2 = True
print('standard error = ' + str(se3))
print('z-value = ' + str(zc))
print('interval = ({}, {})'.format(lb3, ub3))
print(wide2)

# code for question 4
print('Problem 4 Answers:')
# code below this line
tc4 = mean/se
p4 = stats.t.cdf(tc4, df)*2 - 1
print(p4)