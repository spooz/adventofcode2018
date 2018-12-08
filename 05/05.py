class Solution:
    def __init__(self, input_name):
        with open(input_name) as f:
            self.string = f.read().strip()

    def poly_length(self, string):
        stack = []
        for c in string:
            if not stack or stack[-1] != c.swapcase():
                stack.append(c)
            else:
                stack.pop()
        return len(stack)

    def remove(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        min_length = 99999999999
        for removed in alphabet:
            string_with_removed = [c for c in self.string if c != removed and c != removed.swapcase()]
            min_length = min(min_length, self.poly_length(string_with_removed))

        return min_length
