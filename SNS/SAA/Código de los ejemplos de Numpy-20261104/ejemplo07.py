import numpy as np

# Lista: el slice es una copia
l = [1, 2, 3, 4]
l2 = l[:2]
l2[0] = 99
print(l2)      # [1, 2, 3, 4] [99, 2]  
print(l)       # -> la original no cambia

# Array: el slice es una vista
a = np.array([10, 2, 3, 4, 5, 6])
b = a[3:]
b[0] = 40
print(b)   
print(a)  # -> la original sí cambia
