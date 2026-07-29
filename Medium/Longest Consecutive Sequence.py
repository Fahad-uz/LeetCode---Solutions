class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=sorted(nums)
        if not arr:
            return 0
        i=0
        j=1
        win=0
        max_win=0
        while i<j and j<len(nums) and i<len(nums):
            if (arr[j]-arr[i])==1:
                win+=1
                j+=1
                i+=1
            elif (arr[j]-arr[i]==0):
                i+=1
                j+=1
            else:
                i+=1
                j+=1
                win=0
            max_win=max(max_win,win)
        return max_win+1
