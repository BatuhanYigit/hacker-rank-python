students = []


def addToList(name, score):

    students.append([name, score])


if __name__ == "__main__":
    for _ in range(int(input())):
        name = input()
        score = float(input())
        addToList(name, score)

    scores = [student[1] for student in students]

    uniqe_scores = sorted(set(scores))

    second_lowest = uniqe_scores[1]

    second_lowest_students = [
        student[0] for student in students if student[1] == second_lowest
    ]

    second_lowest_students.sort()

    for name in second_lowest_students:
        print(name)
