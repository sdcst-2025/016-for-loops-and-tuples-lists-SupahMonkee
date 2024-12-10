#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
nums = (5,-2,12,-8,14,16)

import math

for i in range(len(nums)):
    if nums[i] > 0:
        sq = math.sqrt(nums[i])
        print(f'The squareroot of {nums[i]} is {sq}.')

#done