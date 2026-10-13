125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.



My Solution

```python
class Solution:
	def isPalindrome(self, s: str) -> bool:
		left, right = 0, len(s) - 1
		while left < right:
			while left < right and not self.alphaNumeric(s[left]):
				left += 1
			while left < right and not self.alphaNumeric(s[right]):
				right -= 1
			if s[left].lower() != s[right].lower():
				return False
			left += 1
			right -= 1
		return True

	def alphaNumeric(self, c):
		return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
```

### How it works

I use two pointers: `left` starts at the beginning of the string and `right` starts at the end. The inner loops move past any character that is not an ASCII letter or digit. Then I compare the remaining characters without worrying about uppercase versus lowercase. If a pair does not match, the string is not a palindrome; otherwise, I move both pointers toward the center. If the pointers meet or cross, every relevant pair matched, so the string is a palindrome.

### Why use a helper function?

`alphaNumeric` puts the character check in one place. Both pointers need the same rule, so the helper avoids repeating the range checks in both loops and makes the main method easier to read. It is mainly for organization and reuse; a function by itself does not reduce the algorithm's space complexity.

### Why not build a cleaned string or use other shortcuts?

Another approach is to remove punctuation, make a lowercase copy, and compare that result with its reverse. That can be concise, but it creates one or more strings proportional to the input length, so it uses `O(n)` extra space. The two-pointer approach checks the original string in place and only keeps two indexes, so it uses `O(1)` extra space. It also returns as soon as it finds a mismatch.

### Why check ASCII ranges instead of using `isalnum()`?

The problem guarantees printable ASCII input. `alphaNumeric` uses `ord()` to check the exact ranges for `A-Z`, `a-z`, and `0-9`, so punctuation and spaces are skipped and only the characters the problem considers alphanumeric are compared. Python's `isalnum()` also recognizes many Unicode letters and digits outside ASCII. The explicit check keeps the accepted character set aligned with this problem's constraint. `.lower()` is still used to make the letter comparison case-insensitive.

### Complexity

- Time: `O(n)`, because each pointer only moves inward through the string.
- Extra space: `O(1)`, because the solution does not create a cleaned or reversed copy of the string.

