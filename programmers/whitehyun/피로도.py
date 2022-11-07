#
#  피로도
#  https://school.programmers.co.kr/learn/courses/30/lessons/87946
#  Version: Python 3.8.13
#
#  Created by WhiteHyun on 2022/11/07.
#

max_count = 0


def recursion(length: int, fatigue: int, dungeons: list, used: list, count: int):
    global max_count

    if length == len(dungeons):
        if max_count < count:
            max_count = count
        return

    for i in range(len(dungeons)):
        if used[i] == False:
            used[i] = True
            if fatigue >= dungeons[i][0]:
                recursion(
                    length + 1, fatigue - dungeons[i][1], dungeons, used, count + 1
                )
            else:
                recursion(length + 1, fatigue, dungeons, used, count)
            used[i] = False


def solution(k: int, dungeons: list) -> int:
    global max_count

    used = [False] * len(dungeons)
    recursion(0, k, dungeons, used, 0)

    return max_count


if __name__ == "__main__":
    ks = [80]
    dungeons = [[[80, 20], [50, 40], [30, 10]]]
    answers = [3]

    for k, dungeon, answer in zip(ks, dungeons, answers):
        predicted_value = solution(k, dungeon)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
