# źle coś
class Node:
    def __init__(self):
        self.val = None
        self.next = None

def SortH(p, k):
    if not p or k == 0:
        return p

    dummy = Node()
    dummy.next = p
    current = dummy

    while current.next:
        min_node = current.next
        prev_min = current
        runner = current.next
        i = 0

        while runner and i <= k:
            if runner.val < min_node.val:
                min_node = runner
                prev_min = current if i == 0 else prev_min.next
            runner = runner.next
            i += 1


        if min_node != current.next:
            prev_min.next = min_node.next
            min_node.next = current.next
            current.next = min_node

        current = current.next

    return dummy.next


# Helper function to convert a list to a linked list
def list_to_linked(lst):
    if not lst:
        return None
    head = Node()
    head.val = lst[0]
    current = head
    for val in lst[1:]:
        new_node = Node()
        new_node.val = val
        current.next = new_node
        current = new_node
    return head

# Helper function to convert a linked list back to a Python list
def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Function to run a test case
def run_test(input_list, k, expected_output):
    head = list_to_linked(input_list)
    sorted_head = SortH(head, k)
    output_list = linked_to_list(sorted_head)
    assert output_list == expected_output, f"Failed for input {input_list} with k={k}. Got {output_list}, expected {expected_output}"
    print(f"Passed for input {input_list} with k={k}.")

# Test Case 1: Already sorted list
run_test([1, 2, 3, 4, 5], 2, [1, 2, 3, 4, 5])

# Test Case 2: Reversed list
run_test([5, 4, 3, 2, 1], 2, [1, 2, 3, 4, 5])

# Test Case 3: Random shuffled list
run_test([4, 3, 2, 6, 5], 2, [2, 3, 4, 5, 6])

# Test Case 4: List with duplicates
run_test([3, 1, 2, 1, 3], 2, [1, 1, 2, 3, 3])

# Test Case 5: Single element
run_test([1], 1, [1])

# Test Case 6: Two elements (unsorted)
run_test([2, 1], 1, [1, 2])

# Test Case 7: Empty list
run_test([], 3, [])

# Test Case 8: Large k value
run_test([4, 3, 2, 1, 5], 4, [1, 2, 3, 4, 5])





