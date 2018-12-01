import itertools

class Solution:
    def __init__(self, input_name):
        with open(input_name) as f:
            self.numbers = f.readlines()
        self.numbers = list(map(lambda x: int(x), self.numbers))

    def sol1(self):
        return sum(self.numbers)

    def sol2(self):
        sum = 0
        visited_numbers = set()
        numbers_inf = itertools.cycle(self.numbers)
        for x in numbers_inf:
            sum = sum + x
            if(sum in visited_numbers):
                return sum
            visited_numbers.add(sum)
