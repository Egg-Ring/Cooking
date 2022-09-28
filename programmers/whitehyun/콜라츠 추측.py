#
#  콜라츠 추측
#  https://school.programmers.co.kr/learn/courses/30/lessons/12943
#  Version: Python 3.8.13
#
#  Created by whitehyun on 2022/09/28.
#


def solution(number: int) -> int:
    task_count = 0
    while task_count < 500:
        if number == 1:
            return task_count

        number = number >> 1 if not number & 1 else number * 3 + 1
        task_count += 1

    return -1


if __name__ == "__main__":
    values = [6, 16, 626331]
    answers = [8, 4, -1]

    for value, answer in zip(values, answers):
        assert solution(value) == answer

