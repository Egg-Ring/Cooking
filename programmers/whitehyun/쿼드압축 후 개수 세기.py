#
#  쿼드압축 후 개수 세기
#  https://school.programmers.co.kr/learn/courses/30/lessons/68936
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/03.
#


def recursion(matrix: list, value: list) -> list:

    if all(map(lambda x: x.count(0) == len(matrix), matrix)):
        value[0] += 1
        return value

    if all(map(lambda x: x.count(1) == len(matrix), matrix)):
        value[1] += 1
        return value

    half = len(matrix) >> 1

    quadrant1 = recursion([*map(lambda x: x[:half], matrix[:half])], value)  # 1사분면
    quadrant2 = recursion([*map(lambda x: x[:half], matrix[half:])], value)  # 2사분면
    quadrant3 = recursion([*map(lambda x: x[half:], matrix[:half])], value)  # 3사분면
    quadrant4 = recursion([*map(lambda x: x[half:], matrix[half:])], value)  # 4사분면

    return value


def solution(arr: list) -> list:
    answer = [0, 0]

    answer = recursion(arr, answer)
    return answer


if __name__ == "__main__":
    matrices = [
        [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]],
        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 1],
        ],
    ]
    answers = [[4, 9], [10, 15]]

    for matrix, answer in zip(matrices, answers):
        predicted_value = solution(matrix)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
