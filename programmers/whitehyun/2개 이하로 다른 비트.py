#
#  2개 이하로 다른 비트
#  https://school.programmers.co.kr/learn/courses/30/lessons/77885
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/02.
#


def solution(numbers: list) -> list:
    answer = []
    for number in numbers:
        binary_number = "0" + bin(number)[2:]
        for bit in range(len(binary_number) - 1, -1, -1):
            if binary_number[bit] == "1":
                continue

            if bit == len(binary_number) - 1:
                binary_number = binary_number[:bit] + "1"
            else:
                binary_number = binary_number[:bit] + "10" + binary_number[bit + 2 :]
            break

        answer.append(int(binary_number, 2))

    return answer


if __name__ == "__main__":
    numbers = [[2, 7]]
    answers = [[3, 11]]

    for number, answer in zip(numbers, answers):
        predicted_value = solution(number)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
