#
#  2개 이하로 다른 비트
#  https://school.programmers.co.kr/learn/courses/30/lessons/77885
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/02.
#

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(get_min_number_of_different_two_bits(number))
    return answer


def get_min_number_of_different_two_bits(number):
    binary = '0' + bin(number)[2:]
    binary_list = list(binary)
    index_zero = binary.rfind('0')
    binary_list[index_zero] = '1'

    if number & 1 == 1:
        binary_list[index_zero + 1] = '0'

    return int(''.join(binary_list), 2)


if __name__ == "__main__":
    numbers = [[2, 7]]
    answers = [[3, 11]]

    for numbers, answer in zip(numbers, answers):
        predicted_value = solution(numbers)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
