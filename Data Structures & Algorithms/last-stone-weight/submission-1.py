class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heap.append(-stone)
        heapq.heapify(heap)
        while len(heap)>1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                difference = first-second
                heapq.heappush(heap,-difference)
        if heap:
            return -heap[0]
        return 0