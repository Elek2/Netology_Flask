case1 = [3, 2, 4]


def twosum(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        remain = target - num
        if remain in nums[i+1:]:
            return [i, nums.index(remain, i+1)]




print(twosum(case1, 6))
