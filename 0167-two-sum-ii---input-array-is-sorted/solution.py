class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}
        for i in range(1, len(numbers) + 1):
            rem = target - numbers[i - 1]
            if rem in table:
                return [table.get(rem), i]
            else:
                table[numbers[i - 1]] = i
