#
#  삼각 달팽이
#  https://school.programmers.co.kr/learn/courses/30/lessons/68645
#  Version: Python 3.9.6
#
#  Created by hobreakb on 2022/11/02.
#

def solution(n):
    road = [[0 for _ in range(n)] for _ in range(n)]

    # 아래로, 오른쪽으로, 왼쪽 위로
    direction = [[1, 0], [0, 1], [-1, -1]]
    direction_index = 0
    x, y, value = 0, 0, 1

    while True:
        if x < 0 or y < 0 or x > n-1 or y > n-1 or road[x][y] != 0:
            break

        road[x][y] = value

        if x + direction[direction_index][0] < 0 or x + direction[direction_index][0] >= n or y + direction[direction_index][1] < 0 or y + direction[direction_index][1] >= n or road[x + direction[direction_index][0]][y + direction[direction_index][1]] != 0:
            direction_index = (direction_index + 1) % 3

        x += direction[direction_index][0]
        y += direction[direction_index][1]
        value += 1

    answer = list(filter(lambda x: x > 0, sum(road, [])))
    return answer


if __name__ == "__main__":
    n = [1, 2, 3, 4, 6]
    answers = [[1], [1, 2, 3], [1, 2, 6, 3, 4, 5], [1, 2, 9, 3, 10, 8, 4, 5, 6, 7], [1, 2, 15, 3, 16, 14, 4, 17, 21,
               13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]]

    for n, answer in zip(n, answers):
        predicted_value = solution(n)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
