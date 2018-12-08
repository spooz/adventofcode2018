class Solution:
    def __init__(self, input_name):
        with open(input_name) as f:
            self.strings = f.readlines()
        self.strings = [x.strip() for x in self.strings]

    def sol1(self):
        twos = 0
        threes = 0

        for s in self.strings:
            letters = self.build_dict(s)
            found_two, found_three = self.find_twos_threes(letters)
            if found_two:
                twos = twos + 1
            if found_three:
                threes = threes + 1

        return twos * threes

    def sol2(self):
        for s in self.strings:
            for z in self.strings:
                differ = 0
                for c1, c2 in zip(s, z):
                    if c1 != c2:
                        differ = differ + 1
                if differ == 1:
                    ans = [ch for idx, ch in enumerate(s) if z[idx] == ch]
                    return ''.join(ans)

    def find_twos_threes(self, letters):
        found_two = False
        found_three = False
        for char, count in letters.items():
            if count == 2:
                found_two = True
            if count == 3:
                found_three = True
        return found_two, found_three

    def build_dict(self, s):
        letters = dict()
        for c in s:
            letters[c] = letters.get(c, 0) + 1
        return letters
