# Definition for singly-linked list node (LeetCode usually provides this).
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1,
        l2 
    ):
        # “Dummy head” to simplify list‐construction logic
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Continue as long as there is a node in l1 or l2, or a nonzero carry
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10

            # Create a new node with the digit (total % 10)
            current.next = ListNode(total % 10)
            current = current.next

            # Advance l1 and l2 if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the head of the newly formed list
        return dummy.next

# Helper to build linked list from Python list
def build_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to convert linked list back to Python list
def list_to_array(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

# Main test harness
def main():
    sol = Solution()
    test_cases = [
        # Basic examples
        ([2,4,3], [5,6,4], [7,0,8]),
        ([0], [0], [0]),
        # Large difference in lengths
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
        # No carry
        ([1,2,3], [4,5,6], [5,7,9]),
        # Single-digit carry
        ([5], [5], [0,1]),
        # One list longer
        ([1,8], [0], [1,8]),
        # Carry propagates to new most significant digit
        ([9,9], [1], [0,0,1]),
        # Equal-length full carry ripple
        ([9,9,9], [9,9,9], [8,9,9,1]),
    ]
    for l1_arr, l2_arr, expected in test_cases:
        l1 = build_list(l1_arr)
        l2 = build_list(l2_arr)
        result_node = sol.addTwoNumbers(l1, l2)
        result_arr = list_to_array(result_node)
        print(f"l1 = {l1_arr}, l2 = {l2_arr}")
        print(f"Expected: {expected}, Got: {result_arr}")
        print("-" * 40)

if __name__ == "__main__":
    main()