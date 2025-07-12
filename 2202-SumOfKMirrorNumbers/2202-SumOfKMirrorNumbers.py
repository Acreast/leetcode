# Last updated: 7/12/2025, 11:47:45 PM

class Solution:
    def is_palindrome(self, num, base):
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    def generate_palindromes(self, num, odd):
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.generate_palindromes(i, True)
                if self.is_palindrome(p, k):
                    total += p
                    n -= 1
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.generate_palindromes(i, False)
                if self.is_palindrome(p, k):
                    total += p
                    n -= 1
            length *= 10
        return total

