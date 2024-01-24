import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    temp = searchstring.split(' ', 1)
    if temp[0] == '+1' or temp[0] == '+52':
        p1 = re.compile('\(\d{3}\)\s\d{3}-\d{4}$')
        p2 = re.compile('\d{10}$')
        p3 = re.compile('\d{3}-\d{3}-\d{4}$')
        r1 = p1.match(temp[1])
        r2 = p2.match(temp[1])
        r3 = p3.match(temp[1])
        valid = ((r1 is not None) or (r2 is not None)) or (r3 is not None)
    elif '+' in temp[0]:
        valid = False
    else:
        if sum(c.isdigit() for c in searchstring) == 7:
            p = re.compile('\d{3}-\d{4}$')
            valid = True if p.search(searchstring) else False
        else:
            valid = False
    return valid

    pass
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    p = re.compile("\d+\s?(?:[A-Z][a-z]*\s?)+(?:Ave|Dr|Rd|St)\.")
    name = p.search(searchstring).group()
    print(name)
    p = re.compile("(?:Ave|Dr|Rd|St)\.")
    result = p.sub("", name)
    return result.strip()
    pass
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """

    a = re.split('(?=\d{3})', searchstring)
    b = re.split('((?:Ave|Dr|Rd|St)\.)', a[1])
    c = re.split('(?=[A-Z][a-z])', b[0], 1)
    target = c[1].strip()
    final = re.sub(c[1], target[::-1] + " ", a[1])
    result = str(a[0]) + str(final)
    return result.strip()
    pass


if __name__ == '__main__' :
    print("\nProblem 1:")
    print("Answer correct?", problem1('+1 765-494-4600') == True)
    print("Answer correct?", problem1('+52 765-494-4600 ') == False)
    print("Answer correct?", problem1('+1 (765) 494 4600') == False)
    print("Answer correct?", problem1('+52 (765) 494-4600') == True)
    print("Answer correct?", problem1('+52 7654944600') == True)
    print("Answer correct?", problem1('494-4600') == True)

    print("\nProblem 2:")
    print("Answer correct?",problem2('Please flip your wallet at 465 Northwestern Ave.') == "465 Northwestern")
    print("Answer correct?",problem2('Meet me at 201 South First St. at noon') == "201 South First")
    print("Answer correct?",problem2('Type "404 Not Found St" on your phone at 201 South First St. at noon') == "201 South First")
    print("Answer correct?",problem2("123 Mayb3 Y0u 222 Did not th1nk 333 This Through Rd. Did Y0u Ave.") == "333 This Through")
    print("Answer correct?",problem2("1 Aa B C D E F St.") == "1 Aa B C D E F")

    print("\nProblem 3:")
    print("Answer correct?",problem3('The EE building is at 465 Northwestern Ave.') == "The EE building is at 465 nretsewhtroN Ave.")
    print("Answer correct?",problem3('Meet me at 201 South First St. at noon') == "Meet me at 201 tsriF htuoS St. at noon")
 