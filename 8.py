# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        no_of_nodes = self.getNoOfNodes(head, 0)

        middle_node_index = no_of_nodes // 2
        middle_node = head
        for i in range(middle_node_index):
            middle_node = middle_node.next
        return middle_node

    def getNoOfNodes(self, head, no_of_nodes):
        if head.next is None:
            return no_of_nodes + 1

        return self.getNoOfNodes(head.next, no_of_nodes + 1)


if __name__ == "__main__":
    # [1,2,3,4,5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().middleNode(head).val)

    # [1,2,3,4,5,6]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(Solution().middleNode(head).val)

    # [1]
    head = ListNode(1)
    print(Solution().middleNode(head).val)

    # [1,2]
    head = ListNode(1)
    head.next = ListNode(2)
    print(Solution().middleNode(head).val)
