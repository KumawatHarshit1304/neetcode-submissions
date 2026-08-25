class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                length=1
                curr=num+1
                while curr in num_set:
                    length+=1
                    curr = curr+1
                longest = max(length,longest)
        return longest