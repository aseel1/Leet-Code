class Solution(object):
    def lengthOfLongestSubstring(self, s):

        
        lastIndex = set()
        left_pointer = 0
        max_len=0
        for right_pointer, digit in enumerate(s) :   #num = index and digit is s[num]
            
            if digit in lastIndex and lastIndex[digit] >= left_pointer:
                left_pointer = lastIndex[digit]
                
            lastIndex[digit] = right_pointer  # always adcance and put the right digit in the window
            
            current_len = right_pointer - left_pointer +1
            if current_len > max_len:
                max_len = current_len
        return max_len        