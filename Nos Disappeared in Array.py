#TC: O(n) where n is the len of the array
#SC: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # utilizing the fact that there are no negative numbers
        
        ans = []
        
        i = 0
        while i < len(nums):
            index = abs(nums[i]) - 1

            if nums[index] > 0:
                nums[index] = nums[index] * -1

            i+= 1

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
            
        return ans