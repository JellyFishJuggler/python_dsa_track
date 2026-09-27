class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        self.head = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

llist = ll()
head = llist.head
head = a

curr = head
while curr != None:
    print(curr)
    print(curr.data)
    curr = curr.next

head = head.next

curr1 = head
while curr1 != None:
    print(curr1)
    print(curr1.data)
    curr1 = curr1.next



# print('Traveral:\n')

    
# print('Insertion:\n')
# newNode = Node(5)
# newNode.next = head
# head = newNode

# nn = Node(40)

# n_curr = head
# while n_curr != None:
#     if n_curr.next == None:
#         nn.next = None
#         n_curr.next = nn
#         break
#     n_curr = n_curr.next
    
# new_curr = head
# nnn = Node(15)

# nnn.next = a.next
# a.next = nnn