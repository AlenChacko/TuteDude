# .py files is a modules that containes code
# types of modules
# 1.Built-in modules
# 2.User defined modules
# 3.Third party modules

"""
Built-in modules: These are already available with Python, no installation requiered.
It is optimized and reliable.Python has 200+ built-in modules

importing modules
1. import module -> importing entire module
2. from modules import func1,func2 -> import specific items
3. import module as mod ->import with alias
4.from module import -> import everything, not recommended
"""

import math

print(math.pi)
print(math.factorial(5))
print(math.sqrt(49))
print(math.ceil(4.2))
print(math.floor(4.9))


# modules documentation
print(help(math))


import random


print(random.randint(1, 10))
print(random.choice(["apple", "banana", "orange"]))
print(random.shuffle([1, 2, 3, 4]))  # modifies list

from datetime import datetime, date

now = datetime.now()
print(now)

today = date.today()
print(today)

import time

print(time.time())
time.sleep(2)
print("Done")

import os

print(os.getcwd())  # current directory

import sys

print(sys.version)
print(sys.path)
sys.exit()
