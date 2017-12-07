class Solution(object):
    def simplifyPath(self, path):
        #利用堆栈
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        ans = ''
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != '/':
                end += 1
            sub = path[i + 1:end]
            if len(sub) > 0:
                if sub == '..':
                    if stack != []:
                        stack.pop()
                elif sub != '.':
                    stack.append(sub)
            i = end
        if stack == []:
            return '/'
        for i in stack:
            ans += '/' + i
        return ans