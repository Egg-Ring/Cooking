#
#  할인 행사
#  https://school.programmers.co.kr/learn/courses/30/lessons/131127
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/01.
#


def solution(want: list, number: list, discount: list) -> int:
    count = 0
    for i in range(len(discount) - 9):
        item_list = discount[i : i + 10]
        for j in range(len(want)):
            if item_list.count(want[j]) != number[j]:
                break
        else:
            count += 1

    return count


if __name__ == "__main__":
    wants = [["banana", "apple", "rice", "pork", "pot"], ["apple"]]
    numbers = [[3, 2, 2, 2, 1], [10]]
    discounts = [
        [
            "chicken",
            "apple",
            "apple",
            "banana",
            "rice",
            "apple",
            "pork",
            "banana",
            "pork",
            "rice",
            "pot",
            "banana",
            "apple",
            "banana",
        ],
        [
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
        ],
    ]
    answers = [3, 0]

    for want, number, discount, answer in zip(wants, numbers, discounts, answers):
        predicted_value = solution(want, number, discount)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

