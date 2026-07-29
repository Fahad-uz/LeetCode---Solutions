class Solution:
    def maxArea(self, height: List[int]) -> int:
        j=len(height)-1
        i=0
        water=0
        while (i<=j):
            if height[i]>height[j]:
                water=max(water,height[j]*(j-i))
                j-=1
            else:
                water=max(water,height[i]*(j-i))
                i+=1
        return water
