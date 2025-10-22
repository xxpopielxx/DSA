class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head):
    mid = find_middle(head)
    left = head
    right = mid.next
    mid.next = None

    left_sorted = sortLinkedList(left)
    right_sorted = sortLinkedList(right)

    return merge(left_sorted, right_sorted)


def find_middle(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(A,B):
    dummy = Node(0)
    current = dummy

    while A and B:
        if A.val < B.val:
            current.next = A
            A = A.next
        else:
            current.next = B
            B = B.next
        current = current.next

    if A:
        current.next = A
    elif B:
        current.next = B

    return dummy.next

def find_run_end(head):
    while head.next and head.val <= head.next.val:
        head = head.next
    return head

def natural_merge_sort(head): #nie wiadomo czy dobrze
    if not head or not head.next:
        return head

    while True:

        run1_start = head
        run1_end = find_run_end(head)

        if not run1_end.next:
            break

        run2_start = run1_end.next
        run2_end = find_run_end(run2_start)

        next_run_next = run2_end.next

        run1_end.next = None
        run2_end_next = None

        merged_head = merge(run1_start, run2_end)

        merged_tail = merged_head
        while merged_tail.next:
            merged_tail = merged_tail.next

        merged_tail.next = next_run_next

        prev_run_next = merged_tail

    return head




















