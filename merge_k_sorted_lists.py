# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_nodes = []

        for linked_list in lists:
            while linked_list:
                next_linked = linked_list.next
                all_nodes.append(linked_list)
                linked_list = next_linked

        flatten = sorted(all_nodes, key=lambda n: n.val)

        first = last = ListNode()
        for f in flatten:
            last.next = f
            last = f

        return first.next
