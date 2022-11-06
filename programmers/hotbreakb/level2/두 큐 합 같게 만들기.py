#
#  두 큐 합 같게 만들기
#  https://school.programmers.co.kr/learn/courses/30/lessons/118667
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/03.
#

from collections import deque


def solution(queue1, queue2):
    answer = 0
    que1 = Deque(queue1)
    que2 = Deque(queue2)
    sum_que1 = sum(que1)
    sum_que2 = sum(que2)

    while answer < len(queue1) * 4:
        if sum_que1 == sum_que2:
            return answer
        elif sum_que1 < sum_que2:
            que1.append(que2.popleft())
            sum_que1 += que1[-1]
            sum_que2 -= que1[-1]
        else:
            que2.append(que1.popleft())
            sum_que2 += que2[-1]
            sum_que1 -= que2[-1]
        answer += 1

    return -1


if __name__ == "__main__":
    queue1 = [[3, 2, 7, 2], [1, 2, 1, 2], [1, 1]]
    queue2 = [[4, 6, 5, 1], [1, 10, 1, 2], [1, 5]]
    answers = [2, 7, -1]

    for queue1, queue2, answer in zip(queue1, queue2, answers):
        predicted_value = solution(queue1, queue2)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
