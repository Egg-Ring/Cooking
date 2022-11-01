#
#  구명보트
#  https://school.programmers.co.kr/learn/courses/30/lessons/42885
#  Version: Python 3.8.13
#
#  Created by whitehyun on 2022/10/31.
#


def solution(people: list, limit: int) -> int:
    sorted_people = sorted(people)
    start = 0
    end = len(sorted_people) - 1
    count = 0

    while start <= end:
        count += 1
        if sorted_people[start] + sorted_people[end] > limit:
            end -= 1
            continue
        end -= 1
        start += 1

    return count


if __name__ == "__main__":

    inputs = [[70, 50, 80, 50], [70, 80, 50], [10, 20, 30, 40], [40, 40, 40, 40]]
    limits = [100, 100, 50, 240]
    answers = [3, 3, 2, 2]

    for input_value, limit, answer in zip(inputs, limits, answers):
        predicted_value = solution(input_value, limit)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

