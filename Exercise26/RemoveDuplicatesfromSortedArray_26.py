#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#Return k.
def removeDuplicates(nums: [int]) -> int:
    """Удалить дубли из массива ин-плейс(поставить их в конец) и вернуть кол-во уникальных элементов

    Args:
        nums (List[int]): Сортированный массив с дублями

    Return:
        k (int): Количество уникальных элементов в массиве
    """
    slow, fast = 0, 1
    while fast in range(len(nums)):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow+1] = nums[fast]
            fast += 1
            slow += 1
    return slow+1
