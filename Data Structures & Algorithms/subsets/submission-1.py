class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def dfs(index,current):
            if index == len(nums):
                result.append(current)
                return
            dfs(index+1,current)
            new_current = current + [nums[index]]
            dfs(index+1, new_current)
        dfs(0,[])
        return result