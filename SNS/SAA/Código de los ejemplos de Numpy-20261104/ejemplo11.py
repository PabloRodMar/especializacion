import numpy as np

print(np.zeros(3))       # [0. 0. 0.]
print(np.ones(3))        # [1. 1. 1.]
print(np.zeros((2, 3)))  # tupla = forma deseada

x = np.empty(2)
print(x.shape)           # (2,)   -> los valores son impredecibles
print(x)

print(np.arange(5))            # [0 1 2 3 4]
print(np.arange(2, 11, 3))     # [2 5 8]
print(np.arange(10, 0, -3))    # [10  7  4  1]

print(np.linspace(0, 1, num=5))    # [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0, 10, num=5))   # [ 0.   2.5  5.   7.5 10. ]

x = np.ones(3, dtype=np.int64)
print(x, x.dtype)                    # [1 1 1] int64
print(np.zeros(3, dtype=np.int32).dtype)   # int32
print(np.arange(3).dtype)            # int64  (enteros)
print(np.arange(3.0).dtype)          # float64 (decimales)