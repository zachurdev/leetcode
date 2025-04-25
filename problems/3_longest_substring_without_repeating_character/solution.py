class Solution:
    def findLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

if __name__ == "__main__":
	sol = Solution()

	cases = [
		("asdgsg", 4),
		("bbbbb", 1),
		("weprw", 3),
		("", 0),
	]

for i, (input_str, expected) in enumerate (cases, 1):
	result = sol.findLongestSubstring(input_str)
	print(f"Test Case {i}: input = '{input_str}'")
	print(f"Expected: {expected}, Got: {result}")
	print("PASS" if result == expected else "FAIL")
	print("-" * 40)

