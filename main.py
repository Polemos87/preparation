#
class Stack:

    def __init__(self):
        self.list_stack = []

    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False

    def push(self, item):
        self.list_stack.append(item)

    def pop(self):
        if self.is_empty() == True:
            return None
        removed_item = self.list_stack.pop()
        return removed_item

    def peek(self):
        if not self.list_stack:
            return None
        else:
            index = len(self.list_stack) - 1
            return self.list_stack[index]
    def size(self):
        return len(self.list_stack)


def balanced(case):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = Stack()
    for item in case:
        if item in "{[(":
            stack.push(item)
        elif stack.list_stack and item == pairs[stack.list_stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack.list_stack) == 0


