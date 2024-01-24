from xml.etree.ElementTree import tostring


def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats

    # Write your code here

    # Swap b and h if b > h
    if b > h:
        temp = b
        b = h
        h = temp
    # Return an empty list if n is 0
    if n == 0:
        return []
    # Initialize hist, bin width(w) and a list of ranges(r)
    hist = n * [0]
    w = (h - b) / n
    r = n * [0]
    # Apply different ranges into r to help identify the index
    for idx in range(0, n):
        r[idx] = (b + idx * w, b + (idx + 1) * w)

    # Find where each data belongs to hist
    for i in range(0, len(data)):
        v = data[i]
        # Make sure b < data <= h (b is excluded according to step 6)
        if (v <= b) and (v >= h):
            continue
        else:
            # Run through upper bounds and lower bounds in each range and add 1 for the correct index in hist
            for lb, ub in r:
                # If data is in range[lb, ub), add 1 to hist with the index of the range in r
                if (v >= lb) and (v < ub):
                    hist[r.index((lb, ub))] += 1
                else: 
                    continue

    # return the variable storing the histogram
    # Output should be a list
    return hist

    pass


def happybirthday(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries

    # Write your code here

    # Initialize month_to_all
    month_to_all = {}

    # Use the value in name_to_month as the key
    # Add tuple (name, (day, year, age)) as the value in month_to_all
    # (day, year, age) are values from name_to_day and neme_to_year corresponding to name
    # age = 2022 - year
    for name, i in name_to_month.items():
        month_to_all[str(i)] = (name, (name_to_day[name], name_to_year[name], 2022 - name_to_year[name]))
    
    return month_to_all
        

    # return the variable storing name_to_all
    # Output should be a dictionary

    pass
