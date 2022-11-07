#
#  피로도
#  https://school.programmers.co.kr/learn/courses/30/lessons/87946
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/07.
#

def solution(k, dungeons):
    stack = [(k, dungeons, 0)]
    answer = 0

    while stack:
        energy, not_visited_dungeon, visited_count = stack.pop()
        answer = max(answer, visited_count)
        for dungeon in not_visited_dungeon:
            if energy >= dungeon[0]:
                stack.append(
                    (energy - dungeon[1], list(filter(lambda x: x != dungeon, not_visited_dungeon)), visited_count + 1))

    return answer


if __name__ == "__main__":
    k = [80]
    dungeons = [[[80, 20], [50, 40], [30, 10]]]
    answers = [3]

    for k, dungeons, answer in zip(k, dungeons, answers):
        predicted_value = solution(k, dungeons)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
