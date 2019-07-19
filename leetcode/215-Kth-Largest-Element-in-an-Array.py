class Solution:
    def findKthLargest(self, nums, k):
        def partition(i, j):
            pivotIndex = i
            pivot = nums[i]
            i += 1
            while True:
                while i < j and nums[i] > pivot: i += 1
                while i <= j and nums[j] <= pivot: j -= 1
                if i >= j: break
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivotIndex], nums[j] = nums[j], nums[pivotIndex]
            return j
        def quickSelect(i, j, k):
            if i >= j: return
            mid = partition(i, j)
            if k > mid + 1 - i: quickSelect(mid + 1, j, k - (mid - i + 1))
            elif k < mid + 1 - i: quickSelect(i, mid - 1, k)
        quickSelect(0, len(nums) - 1, k)
        return nums[k - 1]

