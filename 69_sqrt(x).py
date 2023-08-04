"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        first = 0    
        last = x 
        while first <= last:
            middle = (first + last) // 2
            if (middle * middle) <= x < (middle + 1)*(middle + 1):
                return middle
            elif middle * middle > x:
                last = middle
            else:
                first = middle
