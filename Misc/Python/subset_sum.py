'''
Dynamic programming subset sum problem.
'''
from  collections import defaultdict




# Find the number of subarrays that add up to target sum in given set.

def subarray_sum(nums, k):
    '''
    Underlying concept
    
    sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1.
    Made a hashmap and saved as {sum:frequency}. Now following the formula sum(i,j) = sum(0,j)-sum(0,i)  
    if sum(i,j) == k, added it's frequency to the the count.
    '''
    mydict = defaultdict(int)
    count,add=0,0
    mydict[0] = 1
    for i in nums:
        add += i
        if (add-k) in mydict:
            count += mydict[add-k]
        if add in mydict:
            mydict[add] += 1
        else: 
            mydict[add] = 1
    return count

# kadane's algorithm ( Maximum contiguous subarray sum in the given set)
def kadane(nums):
    maxsum = nums[0]
    curr = nums[0]
    for i in nums[1:]:
        curr = max(curr, curr+i)
        maxsum = max(maxsum, curr)

    return maxsum