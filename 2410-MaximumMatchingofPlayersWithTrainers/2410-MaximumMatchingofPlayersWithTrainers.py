# Last updated: 7/13/2025, 10:56:49 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        i = 0
        j = 0
        while j < len(trainers) and i < len(players):
            if trainers[j] >= players[i]:
                res += 1
                i += 1
            j += 1
        return res
            