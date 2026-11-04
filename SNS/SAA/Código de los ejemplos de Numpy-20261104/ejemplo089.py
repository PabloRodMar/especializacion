import numpy as np

help(np.linspace)
# Help on function linspace in module numpy:
#
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, ...)
#     Return evenly spaced numbers over a specified interval.
#     ...

# In [1]: np.linspace?     # muestra la documentación
# In [2]: a = np.array([1, 2, 3, 4, 5, 6])
# In [3]: a?               # tipo, forma y documentación de la clase ndarray

def doble(a):
    '''Devuelve a * 2'''
    return a * 2

print(doble.__doc__)       # Devuelve a * 2
help(doble)

# In [4]: doble?
# Signature: doble(a)
# Docstring: Devuelve a * 2

# In [5]: doble??
# Signature: doble(a)
# Source:
# def doble(a):
#     '''Devuelve a * 2'''
#     return a * 2