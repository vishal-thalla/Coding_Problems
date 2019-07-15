"""
Recently, on the course of algorithms and data structures, Valeriy learned how to use a deque. He built a deque filled with n elements. The i-th element is ai (i = 1,2,…,n). He gradually takes the first two leftmost elements from the deque (let's call them A and B, respectively), and then does the following: if A>B, he writes A to the beginning and writes B to the end of the deque, otherwise, he writes to the beginning B, and A writes to the end of the deque. We call this sequence of actions an operation.

For example, if deque was [2,3,4,5,1], on the operation he will write B=3 to the beginning and A=2 to the end, so he will get [3,4,5,1,2].

The teacher of the course, seeing Valeriy, who was passionate about his work, approached him and gave him q queries. Each query consists of the singular number mj (j=1,2,…,q). It is required for each query to answer which two elements he will pull out on the mj-th operation.

Note that the queries are independent and for each query the numbers A and B should be printed in the order in which they will be pulled out of the deque.

Deque is a data structure representing a list of elements where insertion of new elements or deletion of existing elements can be made from both sides.

Input
The first line contains two integers n and q (2≤n≤105, 0≤q≤3x105) — the number of elements in the deque and the number of queries. The second line contains n integers a1, a2, ..., an, where ai (0≤a_i≤109) — the deque element in i-th position. The next q lines contain one number each, meaning mj (1≤mj≤1018).

Output
For each teacher's query, output two numbers A and B — the numbers that Valeriy pulls out of the deque for the mj-th operation.
"""
n, q = map(int, input().split())
nums = list(map(int, input().split()))
"""
algo:
store the combos until the maximum element reaches the front of the deque
then the order of the rest of the deque only changes by 2nd element going to end
so let cutoff = number of operation which causes the max element to reach front
if mj <= cutoff then output mjth combo stored
if mj > cutoff  then output = (max, (mj-cutoff-1)%(len-1)+1)
"""

m = max(nums)#max element
# print(nums)
# print(m)
ab = []
while nums[0] < m:
    ab.append([nums[0], nums[1]])
    nums.append(nums.pop(1)) if nums[0]>nums[1] else nums.append(nums.pop(0))
# print(ab)

for i in range(q):
    mj = int(input())
    a, b = map(str, ab[mj-1] if mj <= len(ab) else (m, nums[(mj-len(ab)-1)%(len(nums)-1) +1]))
    print(a + " " + b)



    
