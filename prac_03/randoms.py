"""
CP1404 - Practical 3
Demonstrates Python's random module with randint, randrange, and uniform.
"""

import random

# Q: What did you see on line 1?
# A: A random integer between 5 and 20, inclusive of the limits.
# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number possible was 5, and the largest was 20.

# Q: What did you see on line 2?
# A: A random integer between 3 and 10, incrementing by 2. Hence, the possible outputs were 3, 5, 7, and 9.
# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number possible was 3, and the largest was 9.
# Q: Could line 2 have produced a 4?
# A: No

# Q: What did you see on line 3?
# A: A random float between 2.5 and 5.5, inclusive of the lower limit.
# The upper limit may not be included due to floating-point precision.
# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number possible was 2.5, and the largest was 5.5; although inclusion of 5.5 is not guaranteed.

print(random.randint(1, 100))  # print random integer
print(random.uniform(1, 100))  # print random float ; 'b' may or may not be inclusive
