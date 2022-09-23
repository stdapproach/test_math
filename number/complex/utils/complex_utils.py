#
#import numpy as np  # numpy can't load under bazel env' (issue here)

def mknan_float():
    #return np.nan
    return float('Nan')

def mkinf_float():
    return float('Inf')

def mk_i():
    return complex(0, 1)

if __name__ == '__main__':
    print("QQQ_Complex_utils")