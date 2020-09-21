board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    bucet = []

    for move in moves:

        if not board[move - 1][-1] == 0:
            bucet.append(board[move - 1][-1])
            board[move - 1].pop()

        if len(bucet) > 1:
            if bucet[-1] == bucet[-2]:
                bucet.pop()
                bucet.pop()
                answer += 2

    return answer


def solution(board, moves):
    answer = 0
    bucet = []

    for move in moves:
        for j in range(len(board)):
            if board[j][move - 1] != 0:
                bucet.append(board[j][move - 1])
                board[j][move - 1] = 0

                if len(bucet) > 1:
                    if bucet[-1] == bucet[-2]:
                        bucet.pop(-1)
                        bucet.pop(-1)
                        answer += 2
                break

    return answer


print(solution(board, moves))
