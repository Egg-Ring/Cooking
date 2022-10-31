#
#
#  https://programmers.co.kr/learn/courses/30/lessons/42885
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/10/31.
#

def solution(people, limit):
    answer = 0
    people_sorted = sorted(people)
    start, end = 0, len(people_sorted) - 1
    while start < end:
        if people_sorted[start] + people_sorted[end] > limit:
            end -= 1
        else:
            people_sorted[start] = 0
            people_sorted[end] = 0
            start += 1
            end -= 1
            answer += 1
    return answer + (len(people) - people_sorted.count(0))


print(solution([70, 50, 80, 50, 50], 100))
