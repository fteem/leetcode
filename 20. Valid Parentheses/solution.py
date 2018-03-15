class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parens = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        stack = []
        for char in s:
            if char in parens.keys():
                stack.append(char)
            elif char in parens.values():
                if not stack:
                    return False
                pair = stack.pop()
                if char != parens[pair]:
                    return False

        if stack:
            return False
        return True
