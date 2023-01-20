class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
    # Place item at head of the list

    def pushOn(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    # Place an item after another item in the linked list

    def insertAfter(self, prev_node, new_value):
        if prev_node == None:
            print("The given previous node must not be empty")
            return
        # If the prev_node is not empty, create new node
        new_node = Node(new_value)
        # Update the new nodes next pointer to point to the prev_node's next
        new_node.next = prev_node.next
        # update the previous node's next to be new node
        prev_node.next = new_node
    # add a new node to the end of a linked list

    def append_(self, new_value):
        # create new node with a new value
        new_node = Node(new_value)

        # check if the linked list is empty, if so, make this new node the head node
        if self.head is None:
            self.head = new_node

        # if not empty, traverse the linked list and append to the end
        last = self.head

        # While there is a next, point to the next value
        while last.next:
            last = last.next

        # change current last node value to point to the new valie
        last.next = new_node

    def traverse(self):
        temp = self.head
        # while temp is not none, keep running through the list
        while temp:
            print(temp.value)
            temp = temp.next


monthly_list = LinkedList()

monthly_list.pushOn('January')
# weekdays_list.traverse()
monthly_list.append_('Febuarary')
monthly_list.append_('April')
monthly_list.insertAfter(monthly_list.head.next, "March")
monthly_list.append_('May')
monthly_list.append_('June')
monthly_list.append_('July')
monthly_list.append_('August')
monthly_list.append_('September')
monthly_list.append_('October')
monthly_list.append_('November')
monthly_list.append_('December')
monthly_list.traverse()


# Codewars
# Given a list of integers and a single sum value, return the first two values (parse from the left please)
# in order of appearance that add up to form the sum.
# If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

def sum_pairs(ints, s):
    cache = set()
    for i in ints:
        if s-i in cache:
            return [s-i, i]
        cache.add(i)


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
