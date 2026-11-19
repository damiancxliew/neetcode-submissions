class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            if s[l] == " " or not (s[l].isalpha() or s[l].isdigit()):
                l += 1
                continue
            if s[r] == " " or not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
                continue
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True
