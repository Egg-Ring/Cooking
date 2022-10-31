#
#
#  https://programmers.co.kr/learn/courses/30/lessons/131127
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/10/31.
#

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for product_index in range(len(want)):
        want_dict[want[product_index]] = number[product_index]

    for day in range(len(discount)-sum(number)+1):
        temp_want_dict = want_dict.copy()
        for product in discount[day:day+sum(number)]:
            if product in temp_want_dict:
                temp_want_dict[product] -= 1
        temp_want_dict_values = list(filter(lambda x: x > 0,
                                            list(temp_want_dict.values())))
        if len(temp_want_dict_values) == 0:
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
      "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
