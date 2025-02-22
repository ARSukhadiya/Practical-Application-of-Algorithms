from collections import deque

class MyStack:
    def __init__(self):
        # Initialize two deques
        self.queue1 = deque()

    def push(self, x: int) -> None:
        # Add the new element to queue2
        self.queue1.append(x)
        
    def pop(self) -> int:
        
        for i in range(len(self.queue1) - 1):
            self.push(self.queue1.pop())
            
        # Remove the front element from queue1 and return it
        return self.queue1.popleft()
    
    def top(self) -> int:
        for i in range(len(self.queue1) - 1):
            self.push(self.queue1.popleft())
    
        res = self.queue1[0]
        
        return res

    
    def empty(self) -> bool:
        # Check if queue1 is empty
        return not self.queue1

# Example usage:
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False
print(stack.pop())    # Output: 1
print(stack.empty())  # Output: True


# 2
# 2
# False
# 1
# True