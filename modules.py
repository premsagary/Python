# Import
import math

print(math.sqrt(4))

print(dir(math))


print("Different types of Import")

print ("1. Full import : import modulename # This imports all the methods from module")
print("Example")
print ("math.sqrt(4)")


import math

print(math.sqrt(4))

print(math.e)



print ("2. Specific Import")
print("Example")
print("from math import sqrt")

from math import sqrt, e
print(sqrt(9))
print(e)



print ("3. Import with an alias")
print("Example")
print ("Import pandas as pd")

import math as mt  # When you create a module called math :/ # shouldn't do it
mt.sqrt(9)

print ("4. Import everything")
print("Example")
print ("from math import *")

from math import *
print(sqrt(9))
print(e)


# If you want to import math again , just use "reload math"




