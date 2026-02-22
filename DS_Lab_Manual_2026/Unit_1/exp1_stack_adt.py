class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return "Underflow! Stack is empty."
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Meaningful Use: Reverse a string
s = StackADT()
text = "HELLO"

for ch in text:
    s.push(ch)

reversed_text = ""
while not s.isEmpty():
    reversed_text += s.pop()

print("Reversed:", reversed_text)