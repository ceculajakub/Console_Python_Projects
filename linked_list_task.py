
# Program przenoszący na początek te elementy danej jednokierunkowej linked listy, które mają
# parzystą ilość 5 w zapisie ósemkowym.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sys_swap(n): # system conversion and checking parity of fives
    temp = n
    number = 0
    counter = 0
    while temp != 0:
        number = number * 10 + temp % 8
    str_form_number = str(number)
    for i in range(0, len(str_form_number) + 1):
        if str_form_number[i] == 5:
            counter += 1
    if counter % 2 == 0:
        return True
    else:
        return False


def add_begin(first, val):
    new_node = Node(val)
    new_node.next = first.next
    first.next = new_node


def relocating_function(first):
    start = first

    if first.next == None:
        return
    if sys_swap(first.next.val):
        first = first.next

    while first != None and first.next is not None:

        curr_val = first.val


        if sys_swap(first.val):
            add_begin(start, curr_val)

            first.next = first.next.next
        else:
            first = first.next
