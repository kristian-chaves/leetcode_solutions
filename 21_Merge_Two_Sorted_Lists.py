# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
def MergeLists(list1: ListNode, list2: ListNode):
    if not list1 or not list2:
        return list1 or list2
            
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2

l1 = [1,2,4]
l2 = [1,3,4]
print(MergeLists(l1, l2))