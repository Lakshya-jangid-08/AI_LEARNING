# importing module this type exist
# 1
#   import math
#   math.sqrt(16)

# 2
#   from math import sqrt
#   sqrt(16)

# 3
#   from math import *
#   sqrt(16)

# 4
#   import math as m
#   m.sqrt(16)

# import your own package
from Package.math import *
from Package.subPackage.multiply import multiply

print(add(4, 5))
print(subtract(10, 5))
print(multiply(4, 5))
