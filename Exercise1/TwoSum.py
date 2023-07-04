"""В массиве найти индекс двух чисел, сумма которых равна таргету
"""

def twoSum(nums: [int], target: int) -> List[int]:
    hashMap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashMap:
            return i, hashMap[target-nums[i]]
        hashMap[nums[i]] = i
# Time: O(n)
# Space: O(n)
