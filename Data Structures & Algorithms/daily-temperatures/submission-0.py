class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack=[]
        for current_day in range(len(temperatures)):
            while stack and temperatures[current_day]>temperatures[stack[-1]]:
                old_day=stack.pop()
                result[old_day]=current_day-old_day
            stack.append(current_day)
        return result
# time = O(n)
# space = O(n)