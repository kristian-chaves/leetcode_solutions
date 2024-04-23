# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
def MergeLists(list1, List2): 
    bigList = listNode()
    while(list1 != [] or list2 != []):
        x = min(list1, default = 99999)
        y = min(list2, default = 99999)
        if(x <= y):
            bigList.append(list1.pop(0))
        else:
            bigList.append(list2.pop(0))
    return bigList

list1 = [1,2,4]
list2 = [1,3,4]
print(MergeLists(list1, list2))