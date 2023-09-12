# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Easy


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        # calculate length of needle
        # iterate over haystack
        # match offset of haystack with needle
        nl = len(needle)
        for i in range(len(haystack)):
            if haystack[i : i + nl] == needle:
                return i
        return -1

    def another_sol(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre - 1]

            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        n = 0
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n - 1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1
        return -1


haystack = "sadbutsad"
needle = "sad"
# Output: 0

haystack = "leetcode"
needle = "leeto"
# # Output: -1

haystack = "mississippi"
needle = "issip"

haystack = "abcabababc"
needle = "abcab"

sol = Solution()
# print(sol.str_str(haystack, needle))
print(sol.another_sol(haystack, needle))
