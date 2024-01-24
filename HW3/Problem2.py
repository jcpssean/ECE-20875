import scipy.stats as stats
import matplotlib.pyplot as plt
from helper import *
def get_coordinates(data, each_dist):
    # Part B
    """
    :param: np.ndarray, str
    :return: np.ndarray, np.ndarray
    """
    # Your code starts here...
    coordinate = stats.probplot(data, dist = each_dist)
    return coordinate[0]
    pass


def calculate_distance(x, y):
    # Part B

    """
    :param: float, float
    :return: float
    """
    dist = ((x - (x+y)/2)**2 + (y - (x+y)/2)**2)**0.5
    return dist
    # Your code starts here...
    pass


def find_dist(sum_err, dists):
    # Part B
    """
    :param: list[float], list[str]
    :return: str, float
    """
    temp = sum_err[0]
    idx = 0
    for i in range(1, len(sum_err)):
        if sum_err[i] < temp:
            temp = sum_err[i]
            idx = i
    return (dists[idx], temp)
    # Your code starts here...
    pass


def main(data_file):
    """
        Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return 'norm',0.32)
    :param: *.csv file name (str)
    :return: str, float
    """
    # Part B
    data = get_data(data_file)
    dists = ("norm", "expon", "uniform", "wald")
    sum_err = [0] * 4
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist)
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y)
    return find_dist(sum_err, dists)


if __name__ == "__main__":
    for each_dataset in [
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
    ]:
        print(main(each_dataset))
