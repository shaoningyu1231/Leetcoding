# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(minheap, (l.val, i))
        root = ListNode()
        cur = root
        while(minheap):
            val, i = heapq.heappop(minheap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(minheap, (lists[i].val, i))
        return root.next
        
