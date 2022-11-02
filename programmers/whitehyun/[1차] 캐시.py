#
#  [1차] 캐시
#  https://school.programmers.co.kr/learn/courses/30/lessons/17680
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/02.
#

from collections import deque


def solution(cache_size: int, cities: list) -> int:
    if cache_size == 0:
        return len(cities) * 5
    cities = [*map(lambda x: x.upper(), cities)]

    answer = 5
    cache = deque([cities[0]])

    for element in cities[1:]:
        for i in range(len(cache)):
            if element == cache[i]:  # hit!
                answer += 1
                if len(cache) == cache_size:
                    cache.remove(element)
                cache.append(element)
                break
        else:  # miss..
            answer += 5
            if len(cache) == cache_size:
                cache.popleft()
            cache.append(element)

    return answer


if __name__ == "__main__":
    cache_sizes = [2, 3, 3, 2, 5, 2, 0]
    cities = [
        ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
        ],
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
        ],
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
        ["Jeju", "Pangyo", "NewYork", "newyork"],
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
    ]
    answers = [21, 50, 21, 60, 52, 16, 25]

    for cache_size, city, answer in zip(cache_sizes, cities, answers):
        predicted_value = solution(cache_size, city)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
