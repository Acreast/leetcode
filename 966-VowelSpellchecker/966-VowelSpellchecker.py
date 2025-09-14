# Last updated: 9/15/2025, 1:20:54 AM
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def vowelWildcard(s):
            return ''.join('*' if c in 'aeiou' else c for c in s)
        
        exact = set(wordlist)
        caseMap = {}
        vowelMap = {}

        for word in wordlist:
            lower_case = word.lower()
            devowel = vowelWildcard(lower_case)
            if lower_case not in caseMap:
                caseMap[lower_case] = word
            if devowel not in vowelMap:
                vowelMap[devowel] = word

        result = []
        for q in queries:
            if q in exact:
                result.append(q)
            else:
                lower_case = q.lower()
                devowel = vowelWildcard(lower_case)
                if lower_case in caseMap:
                    result.append(caseMap[lower_case])
                elif devowel in vowelMap:
                    result.append(vowelMap[devowel])
                else:
                    result.append("")
        return result