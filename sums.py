case1 = [3, 2, 4]


def twosum(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        remain = target - num
        if remain in nums[i+1:]:
            return [i, nums.index(remain, i+1)]




print(twosum(case1, 6))

import hashlib

strstr = "yurayura"
strstr2 = "yurayura2"

out = hashlib.md5(strstr.encode())
out2 = hashlib.md5(strstr2.encode())

print(out.hexdigest())
print(out2.hexdigest())
print(out.hexdigest() == out2.hexdigest())