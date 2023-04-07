


def recursive_add(L):
    return recursive_add_impl(L, 0)

if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_add(L1))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_add(L2))
    print(recursive_add([ ]))
