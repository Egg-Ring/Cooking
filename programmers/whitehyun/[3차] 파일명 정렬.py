#
#  [3차] 파일명 정렬
#  https://school.programmers.co.kr/learn/courses/30/lessons/17686
#  Version: Python 3.10.6
#
#  Created by whitehyun on 2022/11/02.
#


def splited(element: str) -> list:
    start_index = 0
    end_index = 0
    for i in range(1, len(element)):
        if element[i].isnumeric():
            start_index = i
            break

    for j in range(i + 1, len(element)):
        if not element[j].isnumeric() or i + 6 == j:
            end_index = j
            break

    if end_index == 0:
        return [element[:start_index], element[start_index:], ""]

    return [element[:start_index], element[start_index:end_index], element[end_index:]]


def combine(elements: list) -> str:
    value = ""
    for element in elements:
        value += element
    return value


def solution(files: list):

    answer = list(map(splited, files))
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return list(map(combine, answer))


if __name__ == "__main__":
    files = [
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
        [
            "F-5 Freedom Fighter",
            "B-50 Superfortress",
            "A-10 Thunderbolt II",
            "F-14 Tomcat",
        ],
        ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
        ["O00321", "O49qcGPHuRLR5FEfoO00321"],
        ["asd1", "asd2"],
    ]
    answers = [
        ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"],
        [
            "A-10 Thunderbolt II",
            "B-50 Superfortress",
            "F-5 Freedom Fighter",
            "F-14 Tomcat",
        ],
        ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
        ["O49qcGPHuRLR5FEfoO00321", "O00321"],
        ["asd1", "asd2"],
    ]

    for number, answer in zip(files, answers):
        predicted_value = solution(number)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"

    print("Succeed")
