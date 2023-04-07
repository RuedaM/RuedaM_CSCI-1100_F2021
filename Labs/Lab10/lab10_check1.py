""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""

def closest1(L):
    '''
    Returns the two closest numbers in a list

    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    >>> closest1([ 1, 5, 9000, 400, 379, 90, 23.999999, 9001 , 9000.1 ])
    (9000, 9000.1)
    >>> closest1([7000])
    (None, None)

    '''
    if (len(L) < 2):
        return (None,None)
    else:
        close1 = L[0]
        close2 = L[1]
        distance = abs(L[0]-L[1])
        for index1 in range(len(L)-1):
            for index2 in range(index1+1, len(L)):
                if (abs(L[index1] - L[index2]) < distance):
                    distance = abs(L[index1] - L[index2])
                    close1 = L[index1]
                    close2 = L[index2]
        return (close1, close2)

if __name__ == "__main__":
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    print(closest1(L1))
    print(closest1([ 1, 5, 9000, 400, 379, 90, 23.999999, 9001 , 9000.1]))
    print(closest1([7000]))
