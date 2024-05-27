class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
        
class LinkedList:
    def __init__(self):
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
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            first_half = self.head
        second_half = prev
        while second_half:
            if first_half.value != second_half.value:
                first_half = first_half.next
                return False
            second_half = second_half.next
        return True


def is_palindrome(head: Node) -> bool:
    if not head or not head.next:
      return True
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    first_half = head
    second_half = prev
    while second_half and first_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True


	
	

ll2 = LinkedList()
for value in [1, 2, 3, 4, 5]:
    ll2.append(value)
print(is_palindrome(ll2.head))