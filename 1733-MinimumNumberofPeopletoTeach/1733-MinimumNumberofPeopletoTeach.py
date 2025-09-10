# Last updated: 9/10/2025, 11:26:47 PM
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        friends_to_teach = set()

        for friend1, friend2 in friendships:
            friend1 -= 1
            friend2 -= 1
            can_communicate = False

            for lang in languages[friend1]:
                if lang in languages[friend2]:
                    can_communicate = True
                    break
            
            if not can_communicate:
                friends_to_teach.add(friend1)
                friends_to_teach.add(friend2)
        

        min_teaches = len(languages) + 1

        for language in range(1, n + 1):
            count = 0
            for friend in friends_to_teach:
                if language not in languages[friend]:
                    count += 1
            
            min_teaches = min(min_teaches, count)
        return min_teaches