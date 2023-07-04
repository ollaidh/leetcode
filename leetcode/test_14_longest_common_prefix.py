# Function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


import unittest


class Solution(object):
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = []
        for i in range(0, len(strs[0])):
            for word in strs:
                if len(word) <= i:
                    return "".join(result)
                if word[i] != strs[0][i]:
                    return "".join(result)
            result.append(strs[0][i])

        return "".join(result)


class PrefixTest(unittest.TestCase):
    def test_longestCommonPrefix(self):
        solution = Solution()
        self.assertEqual("fl", solution.longestCommonPrefix(["flower", "flow", "flight"]))
        self.assertEqual("", solution.longestCommonPrefix(["dog", "racecar", "car"]))
        self.assertEqual("racecar", solution.longestCommonPrefix(["racecar", "racecar", "racecar"]))
        self.assertEqual("a", solution.longestCommonPrefix(["ab", "a", "ac"]))


if __name__ == "__main__":
    unittest.main()
