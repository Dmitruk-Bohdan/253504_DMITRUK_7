import os, sys

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

module_dir = os.path.join(parent_dir, "volume", "geometric_lib")

sys.path.append(module_dir)

import square

value = int(os.getenv("SQUARE_SIDE"))

print(f"square side equals: {value}")

square_area = square.area(value)

print(square_area)
