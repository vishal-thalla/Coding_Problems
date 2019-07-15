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



    
