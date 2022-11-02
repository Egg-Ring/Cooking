#
#  [1차] 캐시
#  https://school.programmers.co.kr/learn/courses/30/lessons/17680
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/02.
#


def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        if city.lower() in cache:
            city_index = cache.index(city.lower())
            cache = cache[:city_index] + \
                cache[city_index + 1:] + [city.lower()]
            answer += 1
        else:
            if cacheSize != 0 and len(cache) == cacheSize:
                cache = cache[1:]
            if cacheSize != 0:
                cache.append(city.lower())
            answer += 5

    return answer


if __name__ == "__main__":
    cacheSize = [0, 3, 2, 5, 2, 0, 1]
    cities = [["Jeju", "jeju", "jeju"], ["Jeju", "Pangyo",
                                         "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]]
    answers = [15, 21]

    for cacheSize, cities, answer in zip(cacheSize, cities, answers):
        predicted_value = solution(cacheSize, cities)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
