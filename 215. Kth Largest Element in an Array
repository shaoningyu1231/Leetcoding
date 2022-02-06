# the defination of heap in python => minheap. Thus, to use the maxheap, we have to convert the list elements to minus one. 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        while k != 1:
            heapq.heappop(heap)
            k -= 1
        res = heapq.heappop(heap)
        return -res
        
