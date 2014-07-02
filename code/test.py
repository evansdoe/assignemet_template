# Author: Firstname Middlename LASTNAME
# Email: username@aims.ac.za
# Comment:

#=================Modules======================

#=================Constants====================

#=================Functions====================

def applyToEach(L, x):
    """
    L = list of functions
    x = int or floating point number
    """
    result = []
    for func in L:
        result.append(func(x))
    return result

def square(x):
    """
    x = int or floating point digit
    """
    return x * x

#=================Implementation===============

if __name__ == "__main__":
    print applyToEach([square, abs], -4)
