#
#  큰 수 만들기
#  https://school.programmers.co.kr/learn/courses/30/lessons/42883
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/03.
#

def solution(number, k):
    number_list = list(number)
    stack = []
    index = 0

    while index < len(number):
        # index에 있는 값과 (index+1)에 있는 값을 비교
        appended_index = index
        # (index+1)에 있는 값이 더 크면, 이 값을 append
        if index + 1 < len(number) and number_list[index + 1] > number_list[index] and k > 0:
            appended_index += 1
            # index에 있는 값은 stack에 들어가지 못함
            k -= 1
        # 값을 넣기 전에 stack에 있는 값들과 비교
        while stack and stack[-1] < number_list[appended_index] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number_list[appended_index])
        index = appended_index + 1

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


if __name__ == "__main__":
    number = ["1231234", "4177252841", "1924", "17"]
    k = [3, 4, 2, 1]
    answers = ["3234", "775841", "94", "7"]

    for number, k, answer in zip(number, k, answers):
        predicted_value = solution(number, k)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
