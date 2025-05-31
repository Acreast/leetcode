# Last updated: 5/31/2025, 11:42:47 PM
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def int_to_pos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        q = deque()
        q.append([1, 0])
        visit = set()
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                next_square = square + i
                r, c = int_to_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == length * length:
                    return moves + 1
                if next_square not in visit:
                    visit.add(next_square)
                    q.append([next_square, moves + 1])
        return -1