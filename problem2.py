
# ADD TWO NUMBERS


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes 
# contains a single digit.  Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# l1 = [2,4,3]
# l2 = [5,6,4]

l1 = list(map(int,input("Enter the list of numbers in list 1 separated by space: ").split()))
l2 = list(map(int,input("Enter the list of numbers in list 2 separated by space: ").split()))

l1.reverse()
l2.reverse()
# print(l1)

joined1 = "".join(map(str,l1))
joined2 = "".join(map(str, l2))

# print(joined1)
# print(joined2)
integer1 = int(joined1)
integer2 = int(joined2)
sum = integer1 + integer2
# sum1 = str(sum)
# print(type(sum1))
sum1 = list(str(sum))
# sum1 = list(sum)

sum1.reverse()
new = list(map(int,sum1))

# print(sum)
print(sum1)
print(new)


