#
#  큰 수 만들기
#  https://school.programmers.co.kr/learn/courses/30/lessons/42883
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/03.
#


def solution(number: str, k: int) -> str:
    number_list = [*map(int, [*number[::-1]])]  # [1, 2, 3, 4] 처럼 만듦
    stack = [number_list.pop()]
    while number_list:
        element = number_list.pop()
        while k > 0 and stack and stack[-1] < element:
            stack.pop()
            k -= 1

        stack.append(element)

    while k > 0:
        stack.pop()
        k -= 1

    return "".join(map(str, stack))


if __name__ == "__main__":
    numbers = [
        "1924",
        "1231234",
        "4177252841",
        "1942",
        "1942",
        "517368",
    ]
    ks = [2, 3, 4, 2, 3, 4]
    answers = ["94", "3234", "775841", "94", "9", "78"]

    for number, k, answer in zip(numbers, ks, answers):
        predicted_value = solution(number, k)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
