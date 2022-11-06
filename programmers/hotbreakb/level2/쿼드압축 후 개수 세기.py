#
#  쿼드압축 후 개수 세기
#  https://school.programmers.co.kr/learn/courses/30/lessons/68936
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/03.
#

def solution(arr):
    answer = [0, 0]

    def compression(x, y, length) -> None:
        start = arr[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if start != arr[i][j]:
                    length //= 2
                    compression(x, y, length)
                    compression(x, y + length, length)
                    compression(x + length, y, length)
                    compression(x + length, y + length, length)

                    # 더이상 이중 for문을 돌지 않아야 함
                    return

        answer[start] += 1

    compression(0, 0, len(arr))

    return answer


if __name__ == "__main__":
    arr = [[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]], [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [
        0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]]
    answers = [[4, 9], [10, 15]]

    for arr, answer in zip(arr, answers):
        predicted_value = solution(arr)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
