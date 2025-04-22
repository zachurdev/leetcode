# Bring in the Optional type because LeetCode uses it by default
from typing import Optional

# Define a singly linked list
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val # Use .val to get value of current node
        self.next = next # Use .next to get address of next node

# Simple list(s) of numbers representing values (in reverse order)
l1_vals = [5, 4, 3]
l2_vals = [9, 8, 7, 6]

# Instantiate the l1 and l2 linked lists using the first list values
l1 = ListNode(l1_vals[0])
l2 = ListNode(l2_vals[0])

# Store point to beginning of l1 as variable named tmp1
tmp1 = l1
for num in l1_vals[1:]: # Loop over the l1_vals using num starting at the second list value (index[1])
	tmp1.next = ListNode(num) # Assign next node after current position as the next value in the list
	tmp1 = tmp1.next # Move next node to be the current node

# Do the same thing as the block above, but this time for l2
tmp2 = l2
for num in l2_vals[1:]:
    tmp2.next = ListNode(num)
    tmp2 = tmp2.next

# This part has the actual logic to solve the problem
"""
Make a singly linked list, use tmp3 to store the pointer to i
Define the carryover amount from the addition operations and set it to 0 (in case there is none)
While there is a value in l1, l2, or the carryover amount do some operations
If l1 is populated, use its value. Otherwise use 0 to represent none
If l2 is populated, use its value. otherwise use 0 to represent none
Calculate the total for the current digit
If the number is greater than 10, compute how much value is in the 10s spot (or beyond) and carry it over
Calculate the remainder after dividing by 10 to determine how much goes into the current digit's position
Put the value of the digit variable into the current position of the linked list
Move the cursor along to the next positon in the linked list
If l1 or l2 run out of digits, change them to None types
After completing the while-loop, return the next position of ListNode() named ans
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        tmp3 = ans
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            tmp3.next = ListNode(digit)
            tmp3 = tmp3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next

# Instantiate a Solution class and name it solution
solution = Solution()
# Let the result variable be equal to the result of the solution's addTwoNumbers function when using l1 and l2 as input
result = solution.addTwoNumbers(l1, l2)

# Make a print-friendly list variable named output
output = []
# While result still has next values, append current values to the output list
while result:
    output.append(result.val)
    result = result.next

# Print the output (a simple list) which gives the values in reverse order
print(output)
# Reverse the list, convert digits to strings, join characters, convert string to integer value, and print
print(int("".join(str(d) for d in reversed(output)))) # This gives you a human-readable number

