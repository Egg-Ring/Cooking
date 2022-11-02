#
#  피보나치 수
#  https://school.programmers.co.kr/learn/courses/30/lessons/12945
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/09/28.
#


def solution(number: int) -> int:
    fibonacci_list = [0] * (number + 1)
    fibonacci_list[1] = 1
    for i in range(2, number + 1):
        fibonacci_list[i] = (fibonacci_list[i - 1] + fibonacci_list[i - 2]) % 1234567

    return fibonacci_list[-1]


if __name__ == "__main__":
    values = [2, 3, 4, 5]
    answers = [1, 2, 3, 5]
    for value, answer in zip(values, answers):
        assert solution(value) == answer
