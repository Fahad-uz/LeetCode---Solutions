class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_product=nums[0]
        max_product=nums[0]
        min_product=nums[0]
        for i in nums[1:]:
            old_current_product=current_product
            current_product=max(i,old_current_product*i,min_product*i)
            min_product=min(i,old_current_product*i,min_product*i)
            max_product=max(max_product,current_product)
        return max_product
        
