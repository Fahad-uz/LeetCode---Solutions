class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        first_seen = {0: -1}
        longest = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                balance -= 1
            else:
                balance += 1
            if balance in first_seen:
                length = i - first_seen[balance]
                longest = max(longest, length)
            else:
                first_seen[balance] = i
        return longest
