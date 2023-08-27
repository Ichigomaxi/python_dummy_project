from inspect import _void
from typing import List

class Solution:
    def __compare_and_rearrange__(self, num: int, largest_values_ordered: List[int]):
        """
        Void function
        e.g.
        largest_values_ordered =  [ 10, 3]
        """
        k = len(largest_values_ordered)
        # Check if new number is larger than previous numbers
        for j in range(k): 
            if(num > largest_values_ordered[j]):
                # if larger than the l-th element of the tracked largest values
                # replace the l-th element with new number and push the previous l-th element to the bottom

                # temp_previous_large_value = largest_values_ordered[j]
                largest_values_ordered.insert(j,num)
                largest_values_ordered.pop()



    def findKthLargest(self, nums: List[int], k: int) -> int:
        # largest_values_ordered = [-10 for i in range(3)]
        largest_values_ordered = [-pow(10,4)]*k
        print(largest_values_ordered)

        length_array = len(nums)

        for i in range(length_array):
            
            num = nums[i]
            self.__compare_and_rearrange__(num,largest_values_ordered)
        
        print(largest_values_ordered[-1])
        return largest_values_ordered[-1]

###############################
"""
Main Thread
"""

nums = [3,2,1,5,6,4]
k=2

solution = Solution()

solution.findKthLargest(nums, k)