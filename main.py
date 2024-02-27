
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def balance(expression):
    stack = Stack()
    for char in expression:
        if char in ["(", "{", "["]:
            stack.push(char)
        elif char in [")", "}", "]"]:
            if stack.is_empty():
                return False
            if char == ")" and stack.peek() != "(":
                return False
            elif char == "}" and stack.peek() != "{":
                return False
            elif char == "]" and stack.peek() != "[":
                return False
            stack.pop()
    return stack.is_empty()

if __name__ == "__main__":
    stack = Stack()
    if balance(input("Введите выражение, состоящее из скобок (, {, [: \n")):
        print("Сбалансированно")
    else:
        print("Несбалансированно")