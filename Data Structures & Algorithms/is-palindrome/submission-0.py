class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        def valid(c):
            x = ord(c)
            return (48 <= x <= 57 or
                    65 <= x <= 90 or
                    97 <= x <= 122)

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not valid(s[left]):
                left += 1

            while left < right and not valid(s[right]):
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True