class Solution(object):
    def lengthOfLongestSubstring(self, s):
        final_len = 0

        for i in range(len(s)):
            temp = ""
            count = 0
            while (i + count < len(s)) and s[i + count] not in temp:
                temp += s[i + count]
                count += 1
            if len(temp) > final_len:
                final_len = len(temp)
        return final_len
            
        
def main():
    solution = Solution()
    count = solution.lengthOfLongestSubstring("dvdf")
    print(count)

main()
