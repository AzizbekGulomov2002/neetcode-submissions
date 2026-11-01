class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def dfs():
            if len(current) == len(nums):
                result.append(current.copy())
                return
            for num in nums:
                if num in current:
                    continue
                current.append(num)
                dfs()
                current.pop()
        dfs()
        return result