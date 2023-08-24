## Linked List
- Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.

### Main Concepts
Before going more in depth on what linked lists are and how you can use them, you should first learn how they are structured. Each element of a linked list is called a ```node```, and every node has two different fields:
  1. ```Data``` contains the value to be stored in the node.
  2. ```Next``` contains a reference to the next node on the list.

> [!NOTE]
> A ```linked list``` is a collection of nodes. The first node is called the ```head```, and it’s used as the starting point for any iteration through the list. The last node must have its ```next``` reference pointing to ```None``` to determine the end of the list.
Here’s how it looks:

### Introducing collections.deque
In Python, there’s a specific object in the collections module that you can use for linked lists called deque (pronounced “deck”), which stands for double-ended queue.
```collections.deque``` uses an implementation of a linked list in which you can access, insert, or remove elements from the beginning or end of a list with constant ***O(1) performance***.
```py
from collections import deque

deque()
# deque([])

deque(['a','b','c'])
# deque(['a', 'b', 'c'])

deque('abc')
# deque(['a', 'b', 'c'])

empty = deque()
empty.append('a')
empty.append('b')
empty.append('c')
# deque(['a', 'b', 'c'])

empty.pop()
# deque(['a', 'b'])

empty.appendleft('1')
# deque(['1', 'a', 'b'])

empty.appendleft('2')
# deque(['2', '1', 'a', 'b'])

empty.popleft()
# deque(['1', 'a', 'b'])
```
- Reference(s):
  - https://realpython.com/linked-lists-python/
