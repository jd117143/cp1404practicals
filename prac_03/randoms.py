import random

# Q: What did you see on line 1?
# A: A random integer from 5 to 20, inclusive of the limits.
# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number possible was 5, and the largest was 20.

# Q: What did you see on line 2?
# A: A random integer from 3 to 10 in increments of 2. Hence, the possible outputs were 3, 5, 7, and 9.
# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number possible was 3, and the largest was 9.
# Q: Could line 2 have produced a 4?
# A: No

# Q: What did you see on line 3?
# A: A random float from 2.5 and 5.5, inclusive of the limits.
# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number possible was 2.5, and the largest was 5.5

print(random.randint(1, 100))  # print random integer
print(random.uniform(1, 100))  # print random number; b may or may not be inclusive
