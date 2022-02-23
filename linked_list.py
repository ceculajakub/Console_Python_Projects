
# Dana jest linked lista reprezentująca liczbę naturalną (każdy "Node" zawiera cyfrę).
# Ten program obsługuje tę strukturę i zwiększa tę liczbę o 1.

class Node: # linked list structure
    def __init__(self, val):
        self.val = val
        self.next = None

def print_node(first):
    while first is not None:
        print("->", first.val, end="")
        first = first.next


def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range (n-1, -1, -1):
        temp=Node(tab[i])
        temp.next = first
        first = temp
    return first


def add_to_num(first):
    temp = first
    temp.val += 1
    while temp.val > 9:
        temp.val = 0
        if temp.next == None:
            temp.next = Node(1)
            temp = temp.next
        else:
            temp = temp.next
            temp.val += 1







