class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        def dfs(index,remaining):
            if remaining == 0:
                result.append(current.copy())
                return
            if remaining < 0:
                return
            if index == len(nums):
                return
            # Take
            current.append(nums[index])
            dfs(index,remaining-nums[index])
            # Undo Take
            current.pop()
            # Skip
            dfs(index+1,remaining)
        dfs(0,target)
        return result