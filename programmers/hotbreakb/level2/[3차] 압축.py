#
#  [3차] 압축
#  https://school.programmers.co.kr/learn/courses/30/lessons/17684
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/07.
#


def solution(msg):
    answer = []
    dictionary = {chr(i + 64): i for i in range(1, 27)}
    start, end = 0, 0

    while end < len(msg):
        while msg[start:end+1] in dictionary:
            end += 1
            if end == len(msg):
                answer.append(dictionary[msg[start:end]])
                return answer

        answer.append(dictionary[msg[start:end]])
        dictionary[msg[start:end+1]] = len(dictionary) + 1
        start = end

    return answer


if __name__ == "__main__":
    msg = ["KAKAO", "ABABABABABABABAB", "TOBEORNOTTOBEORTOBEORNOT"]
    answers = [[11, 1, 27, 15],  [1, 2, 27, 29, 28, 31, 30], [20, 15, 2, 5, 15, 18, 14, 15, 20,
                                                              27, 29, 31, 36, 30, 32, 34], ]

    for msg, answer in zip(msg, answers):
        predicted_value = solution(msg)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
