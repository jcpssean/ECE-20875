from cProfile import label
from tkinter import Y
import numpy as np
from matplotlib import pyplot as plt

# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    X = []
    Y = []
    data = []
    f = open(datapath)
    for l in f:
        row = l.split()
        x = float(row[0])
        y = float(row[1])
        data.append((x, y))
    f.close()
    data = sorted(data, key = lambda k: (k[0], k[1]))
    for x, y in data:
        X.append(x)
        Y.append(y)
    plt.scatter(X, Y, label = "data")
    for d in degrees:
        testx = 2
        testy = 0
        newY = []
        coeff = least_squares(feature_matrix(X, d), Y)
        paramFits.append(coeff)
        newY = PolyCoefficients(X, coeff)
        plt.plot(X, newY, label = "degree = " + str(d))
        if d == 3:
            deg = 0
            for i in range(d, -1, -1):
                testy += coeff[deg]*x**i
                deg += 1
            print("testy = " + str(testy))
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    return paramFits

def PolyCoefficients(X, coeff):
    o = len(coeff) - 1
    Y = []
    for x in X:
        y = 0
        d = 0
        for i in range(o, -1, -1):
            y += coeff[d]*x**i
            d += 1
        Y.append(y)
    return Y

    # y = 0
    # d = 0
    # for x in X:
    #     for i in range(o, -1, -1):
    #         y += coeff[d]*(x**i)
    #         d+=1
    # return y


# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):

    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X=[[i**j for j in range(d,-1,-1)] for i in x]

    return X


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)

    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B = np.linalg.lstsq(X,y,rcond=1)[0]
    B = [float(i) for i in B]
    return B


if __name__ == "__main__":
    datapath = "poly.txt"
    degrees = [1, 2, 3, 4, 5]

    paramFits = main(datapath, degrees)
    print(paramFits)
