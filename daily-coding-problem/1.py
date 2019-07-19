"""
Similar with leetcode problem two sum
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
"""
def twoSum(list, target):
    from collections import defaultdict
    rest = defaultdict(int)
    for i in range(len(list)):
        if list[i] in rest: return True
        rest[target - list[i]] = list[i] 
    return False

print(twoSum([10, 15, 3, 7], 17))
print(twoSum([10, 15, 3, 7], 30))
        
