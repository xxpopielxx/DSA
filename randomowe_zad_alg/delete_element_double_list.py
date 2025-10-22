class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def delete_node(head, value):
    if not head:
        return None

    current = head  # Start from the head

    # Search for the node to delete
    while current and current.value != value:
        current = current.next

    # If the node is not found
    if not current:
        return head

    # If deleting the first node (head)
    if not current.prev:
        head = current.next
        if head:
            head.prev = None

    # If deleting a middle or last node
    else:
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    return head  # Return the updated head
