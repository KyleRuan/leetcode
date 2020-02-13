
# 最长回文子串
# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        arr = [[0]*s_len for _ in range(s_len)]
        start,end = 0,0
        str_len_count = 0
        for gap in range(s_len):
            for i in range(s_len-gap):
                j = i + gap
                if s[i:i+1] == s[j:j+1]:
                    if j - i <= 1:
                        arr[i][j] = 1
                    elif j - i >= 2 and arr[i+1][j-1] == 1:
                        arr[i][j] = 1
                    if arr[i][j] == 1 and  j - i > str_len_count:
                        start = i
                        end = j
                        str_len_count = j-i
        return s[start:end+1]
