class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


