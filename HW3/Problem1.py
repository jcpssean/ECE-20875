import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    :param hist: a numpy ndarray object
    :return: list
    """
    norm_h = []
    for i in range(0, len(hist)):
        norm_h.append(hist[i]/sum(hist))
    return norm_h

    pass


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width
    :param histo: list
    :param width: float
    :return: float
    """
    m = sum(histo)
    denominator = (m-1)*width
    norm_h = norm_histogram(histo)
    prob_sum = sum([i**2 for i in norm_h])
    J = 2 / denominator - ((m+1) / denominator) * prob_sum

    return J
    pass


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    lo = minimum
    hi = maximum
    i = 0
    sweep = [0] * (max_bins - min_bins + 1)
    for bin in range(min_bins, max_bins+1):
        width = (hi - lo) / bin
        sweep[i] = compute_j(plt.hist(data, bin, (lo, hi))[0], width)
        i+=1
    return sweep

    pass


def find_min(l):
    """
    takes a list of numbers and returns the mean of the three smallest number in that list and their index.
    return as a tuple i.e. (the_mean_of_the_3_smallest_values,[list_of_the_3_smallest_values])
    For example:
        A list(l) is [14,27,15,49,23,41,147]
        The you should return ((14+15+23)/3,[0,2,4])

    :param l: list
    :return: tuple
    """
    mins = [999, 999, 999, 999]
    idx = [0, 0, 0, 0]
    for i in range(0, len(l)):
        temp = l[i]
        for j in range(0, len(mins)-1):
            if temp < mins[j]:
                mins[j+1] = mins[j]
                idx[j+1] = idx[j]
                mins[j] = temp
                idx[j] = i
                break
    mins.pop()
    idx.pop()
    return (sum(mins)/len(mins), idx)

    pass


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
