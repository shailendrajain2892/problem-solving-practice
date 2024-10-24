import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {1: [],
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z']}

        # digit_list = [int(digit) for digit in digits]
        # digit_letter_map = [letterMap.get(d) for d in digit_list]
        # combinations = list(itertools.product(*digit_letter_map))
        # print(combinations)
        # return [''.join(combo) for combo in combinations]
        result = []
        def backtrack(index, path):
            if index == len(digits):
                result.append(''.join(path))
                return
            current_digit = int(digits[index])
            digit_letters = letterMap.get(current_digit)
            for letter in digit_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
        backtrack(0, [])
        return result


print(Solution().letterCombinations('34'))            