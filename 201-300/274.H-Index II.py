class Solution(object):
    def hIndex(self, citations):
        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            #二分查找
            mid = (low + high) / 2
            if N - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return N - low