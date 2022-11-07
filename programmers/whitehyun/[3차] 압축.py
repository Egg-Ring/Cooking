#
#  [3차] 압축
#  https://school.programmers.co.kr/learn/courses/30/lessons/17684
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/07.
#


def solution(msg: str) -> list:
    answer = []
    dictionary = {chr(number + 64): number for number in range(1, 27)}

    string = ""
    index = 0
    while index < len(msg):
        string += msg[index]
        index += 1
        # key 값이 있으면 다시 반복문으로 직행
        if dictionary.get(string) is not None:
            continue

        # 새롭게 넣은 알파벳을 제외한 문자의 value값 할당
        answer.append(dictionary[string[:-1]])

        # key가 없는 새로운 문자는 마지막으로 갱신한 숫자에서 1 더한 값으로 할당
        dictionary[string] = list(dictionary.items())[-1][1] + 1

        # 마지막 알파벳으로 다시 대체
        string = string[-1]
    else:
        # 반복문 끝나고 마지막에 넣지 못한 알파벳 할당
        answer.append(dictionary[string])

    return answer


if __name__ == "__main__":
    messages = ["KAKAO", "TOBEORNOTTOBEORTOBEORNOT", "ABABABABABABABAB"]
    answers = [
        [11, 1, 27, 15],
        [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34],
        [1, 2, 27, 29, 28, 31, 30],
    ]

    for message, answer in zip(messages, answers):
        predicted_value = solution(message)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
