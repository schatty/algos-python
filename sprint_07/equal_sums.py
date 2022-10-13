"""
https://contest.yandex.ru/contest/25597/run-report/70030471/

----------------------------- Idea ----------------------------

In the description below SUM is the sum over all N given numbers.

Given the N numbers our goal is to find SUM / 2 because this is 
the only option our sums can be equal. To do so, we will keep some
buffer BUF which contains sums seen so far. Initially BUF will 
contain only 0. We iterate through each number and update BUF
to contain new sums each_num_from_buf + new_number. If the new value
is equal to the SUM / 2, we know that there exist two needed sums
(because we know that the sum is equal to SUM and has found a subset
which sums up to SUM/2, therefore there exists another subset that
sums up to SUM/2).

Implementation details:
    * We will use a set as BUF to reduce memory complexity.

------------------------ Time Complexity ----------------------

We need to iterate through each of the element from N given, where
for each element we compare it to the existing BUF, which may contain
no more than SUM elements.

Total: N * SUM

------------------------ Space Complexity ----------------------

We need to sore the BUF for existing current sum which can't be bigger
than SUM (in case we use set which doesn't allow duplicates).

Total: SUM

"""
n = int(input())
nums = list(map(int, input().split()))

def equal_sums_exist(nums):
    sum_all = sum(nums)
    if sum_all % 2 == 1:
        return False

    target = sum_all // 2
    sums = {0}
    for n in nums:
        new_sums = set()
        for sum_old in sums:
            val = sum_old + n
            if val == target:
                return True
            new_sums.add(val)
        sums.update(new_sums)

    return False

print(equal_sums_exist(nums))
