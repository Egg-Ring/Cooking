#
#  [3차] 파일명 정렬
#  https://school.programmers.co.kr/learn/courses/30/lessons/17686
#  Version: Python 3.9.6
#
#  Created by hotbreakb on 2022/11/02.
#

def solution(files):
    keys = []
    for file in files:
        keys.append(find_HEAD(file))

    keys.sort(key=lambda x: (x[1], x[2]))
    return [key[0] for key in keys]


def find_HEAD(file):
    HEAD_index = 0
    for char in file:
        if char.isdigit():
            break
        HEAD_index += 1

    NUMBER_index = HEAD_index
    for i in range(HEAD_index, len(file)):
        if not file[i].isdigit():
            break
        NUMBER_index += 1

    return [file, file[:HEAD_index].lower(), int(file[HEAD_index:NUMBER_index])]


if __name__ == "__main__":
    files = [["img12.png", "img10.png", "img02.png",
             "img1.png", "IMG01.GIF", "img2.JPG"],  ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]]
    answers = [["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"], [
        "A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]]

    for files, answer in zip(files, answers):
        predicted_value = solution(files)
        assert (
            predicted_value == answer
        ), f"{predicted_value} is not correct, answer is {answer}"
