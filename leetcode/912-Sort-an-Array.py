class Solution(object):
    def sortArray(self, nums):
        def merge(left, right, A): # using merge sort :)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    A[k] = left[i]
                    i += 1
                else:
                    A[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                A[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                A[k] = right[j]
                k += 1
                j += 1

        if len(nums) < 2: return nums
        mid = len(nums) >> 1
        left = nums[:mid]
        right = nums[mid:]
        self.sortArray(left)
        self.sortArray(right)
        merge(left, right, nums)
        return nums

