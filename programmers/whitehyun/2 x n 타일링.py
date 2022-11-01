#
#  2 x n 타일링
#  https://school.programmers.co.kr/learn/courses/30/lessons/12900
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/01.
#


def solution(n: int) -> int:
    dp = [0] * 60000
    dp[0] = 1
    dp[1] = 2

    for i in range(2, len(dp)):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1_000_000_007
    return dp[n - 1]


if __name__ == "__main__":
    numbers = [4, 3]
    answers = [5, 3]

    for number, answer in zip(numbers, answers):
        predicted_value = solution(number)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
