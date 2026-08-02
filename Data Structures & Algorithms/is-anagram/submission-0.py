class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Dictionary to store character counts
        count = {}

        # Count every character in s
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # Check every character in t
        for char in t:

            # Character doesn't exist in s
            if char not in count:
                return False

            # Use one occurrence of this character
            count[char] -= 1

            # t has more occurrences than s
            if count[char] < 0:
                return False

        # Everything matched
        return True 