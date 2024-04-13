class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        result = self.stack[-1]
        self.stack.pop()
        return result

    def peek(self):
        result = self.stack[-1]
        return result

    def size(self):
        return len(self.stack)


def balance_brackets(some_string):
    test_stack = Stack()
    for element in some_string:
        if element in "([{":
            test_stack.push(element)

        elif element in "}])":
            if test_stack.size() == 0:
                return "Несбалансированно"
            else:
                if test_stack.peek() == "(" and element == ")":
                    test_stack.pop()
                elif test_stack.peek() == "[" and element == "]":
                    test_stack.pop()
                elif test_stack.peek() == "{" and element == "}":
                    test_stack.pop()
                else:
                    return "Несбалансированно"

    if test_stack.size() == 0:
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == '__main__':
    print(balance_brackets("(5+1)[1[2]{}]"))


