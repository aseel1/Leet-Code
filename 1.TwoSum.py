from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store (number → index)
        index_map = {}

        for i, x in enumerate(nums):
            needed = target - x

            # If the complement is already in the map, we have our answer
            if needed in index_map:
                return [index_map[needed], i]

            # Otherwise, record the current number's index
            index_map[x] = i

        # As per problem constraints, there is always exactly one solution.
        # If we reach here, something is wrong.
        return []



def main():
    sol = Solution()

    # Corrected test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, -2, 8], 6, [0, 1]),      # Corrected: 1 + 5 = 6 → indices [0, 1]
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    for nums, target, expected in test_cases:
        result = sol.twoSum(nums, target)
        print(f"nums = {nums}, target = {target}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    main()