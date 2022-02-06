class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(heap) < k:
                    heapq.heappush(heap, (-(nums1[i] + nums2[j]), [nums1[i], nums2[j]]))
                else:
                    if nums1[i] + nums2[j] < -heap[0][0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-(nums1[i] + nums2[j]), [nums1[i], nums2[j]]))
        res = []
        for i, j in heap:
            res.append(j)
        return res"""
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
            
                
        
