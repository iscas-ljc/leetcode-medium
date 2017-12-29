class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'
    def compare(self, a, b):
        return [1, -1][a + b > b + a]