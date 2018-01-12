class Solution(object):
    def __init__(self):
        self.cache = collections.defaultdict(list)
    def diffWaysToCompute(self, input):
        if input.isdigit(): return [int(input)]
        if input in self.cache: return self.cache[input]
        result = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        result.append(eval(str(l) + c + str(r)))
        self.cache[input] = result
        return result