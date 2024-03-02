"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO

    ##base case
    if x.decimal_val or y.decimal_val == 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    ## retreive size of x and y
    n = max(len(x.binary_vec), len(y.binary_vec))
    n_half = n // 2

    # split x
    num_x = split_number(x.binary_vec)
    x_left = num_x[0]
    x_right = num_x[1]

    # split y
    num_y = split_number(y.binary_vec)
    y_left = num_y[0]
    y_right = num_y[1]

    # recursively multiply left 
    left_mult = subquadratic_multiply(x_left, y_left)
    # recursively multiply right
    right_mult = subquadratic_multiply(x_right, y_right)

    # add x side
    x_add = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
    # add y side
    y_add = BinaryNumber(y_left.decimal_val + y_right.decimal_val)

    # then recursively multiply added decimal values and subtract multiplied values
    next = BinaryNumber(subquadratic_multiply(x_add, y_add).decimal_val - left_mult.decimal_val - right_mult.decimal_val)

    # return result
    return BinaryNumber(bit_shift(left_mult, n).decimal_val + bit_shift(next, n_half).decimal_val + right_mult.decimal_val)

    
    
    
    

    



    
 
    ###



def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000


    

