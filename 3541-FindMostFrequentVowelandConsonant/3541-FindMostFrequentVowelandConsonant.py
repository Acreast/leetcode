# Last updated: 9/13/2025, 8:55:41 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        vowels_list = []
        consonant_list = []
        for c in s:
            if c in vowels:
                vowels_list.append(c)
            else:
                consonant_list.append(c)

        max_vowel_count = Counter(vowels_list).most_common(1)[0][1] if vowels_list else 0
        max_consonant_count = Counter(consonant_list).most_common(1)[0][1] if consonant_list else 0
        return max_vowel_count + max_consonant_count
