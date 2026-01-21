class Solution(object):
    def reverseString(self, s):
        l, h = 0, len(s) - 1

        while l < h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1
