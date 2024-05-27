#bozza esercizio lista palindromo
class Node:
    def _init_(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        # Find the middle of the linked list
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare the first and second half nodes
        first_half = self.head
        second_half = prev
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next

        # Optional: Restore the original list (if needed)
        # current = prev
        # prev = None
        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node

        return True
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(2)
linked_list.append(1)
print(linked_list.is_palindrome())  # Output: True





