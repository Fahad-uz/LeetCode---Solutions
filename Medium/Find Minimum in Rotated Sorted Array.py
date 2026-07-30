class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        if len(nums)==1:
            return nums[0]
        while(low<high):
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            elif nums[mid]<nums[high]:
                high=mid
        return nums[low]
