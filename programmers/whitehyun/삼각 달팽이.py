#
#  삼각 달팽이
#  https://school.programmers.co.kr/learn/courses/30/lessons/68645
#  Version: Python 3.8.13
#
#  Created by whitehyun on 2022/11/02.
#


def solution(number: int) -> list:

    number_list = [[0] * i for i in range(1, number + 1)]
    x, y = 0, 0
    while any(map(lambda x: x.count(0) != 0, number_list)):

        while x < len(number_list) and number_list[x][y] == 0:
            number_list[x][y] = number_list[x - 1][y] + 1
            x += 1

        x -= 1
        y += 1

        while y < len(number_list[x]) and number_list[x][y] == 0:
            number_list[x][y] = number_list[x][y - 1] + 1
            y += 1

        x -= 1
        y -= 2

        while y > 0 and x > 0 and number_list[x][y] == 0:
            number_list[x][y] = number_list[x + 1][y + 1] + 1
            x -= 1
            y -= 1

        x += 2
        y += 1

    answer = []
    for element in number_list:
        answer.extend(element)

    return answer


if __name__ == "__main__":
    numbers = [4, 5, 6]
    answers = [
        [1, 2, 9, 3, 10, 8, 4, 5, 6, 7],
        [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9],
        [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11],
    ]

    for number, answer in zip(numbers, answers):
        predicted_value = solution(number)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    solution(7)
