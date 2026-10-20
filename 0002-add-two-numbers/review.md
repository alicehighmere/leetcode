# 2. Add Two Numbers

## Solution 1: Dummy Node and Carry
```Python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        v
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            current.next = ListNode(total % 10)
            carry = total // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            current = current.next
        
        return dummy.next
```

### Approach
1. Recognise the relationship between reversed linked lists and addition.
    - Each linked list represents a non-negative integer.
    - Digits are stored in reverse order.
    - The head contains the ones digit. Subsequent nodes represent higher place values.
    - Traversing each list matches ordinary addition from right to left.
    - There is no need to reverse the lists or convert them into integers.

2. Calculate each **digit** and propagate the **carry**.
    - Initialise carry = 0.
    - Continue while either list has nodes or carry remains.
    - Retrieve each node’s value. Use 0 if the node does not exist.
    - Calculate total = val1 + val2 + carry.
    - Append total % 10 as the current digit.
    - Update carry = total // 10.
    - Process any remaining carry, even after both lists end.

3. Construct the result using a **dummy node**.
    - Initialise dummy = ListNode(0) as a placeholder.
    - Set current = dummy to track the result’s tail.
    - Create a new ListNode for each calculated digit.
    - Append each node through current.next.
    - Advance current, l1, and l2 independently.
    - Return dummy.next to exclude the placeholder.
    
### Analysis
| Metric | Value | Comment |
|:---:|:---:|---|
| TC | O(max(m,n)) | Each input node is visited once. A final carry may add one iteration. |
| SC | O(max(m,n)) | The output contains at most max(m, n) + 1 nodes. Auxiliary space is O(1), excluding the output. |
| Runtime | 3 ms |
| Memory | 19.12 MB |

***N.B.*** Here, m and n are the lengths of the input lists.

### Insights
- Reversed linked lists naturally support ordinary addition.
    - The initial idea was to match digits by index.
    - The key insight was that reversed lists already start with the least significant digit.
    - Traversing each list therefore matches ordinary column-by-column addition.
    - Different list lengths require no special preprocessing.
    - Missing digits can be treated as 0 during each iteration.

- `dummy` and `current` initially **reference the same node**.
    - `current = dummy` does not copy the node.
    - **Both variables reference the same ListNode object.**
    - Assigning `current.next` modifies that shared node.
    - Therefore, `dummy.next` also reflects the new connection.
    - Advancing `current` changes only its reference.
    - `dummy` stays at the beginning of the result list.

- Linked lists use node references to connect and traverse nodes.
    - Each node stores a value in `.val`.
    - Its `.next` attribute references the next node.
    - Assigning `current.next` connects a new node.
    - Assigning `current = current.next` advances the pointer.
    - This does not remove or move the underlying node.
    - The pointers `l1`, `l2`, and `current` move independently.
    - Checking if `l1` and if `l2` prevents accessing `.next` on None.

- The dummy node simplifies result construction.
    - Without a dummy node, the first insertion needs special handling.
    - The dummy provides a stable starting point.
    - Every result digit can then use the same insertion logic.
    - current tracks the tail for efficient appending.
    - dummy.next references the first actual result node.
    - Returning dummy.next excludes the placeholder.
    - The dummy’s value is arbitrary because it is never returned.