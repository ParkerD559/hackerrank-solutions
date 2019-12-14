"""
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the
second lowest grade.

Note: If there are multiple students with the same grade, order their names
alphabetically and print each name on a new line.
"""
import bisect
from collections import defaultdict

if __name__ == "__main__":
    score_to_names = defaultdict(list)
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        # Insert score to sorted list
        bisect.insort(scores, score)
        # Insert name into sorted list of names
        bisect.insort(score_to_names[score], name)

    second_min = next(
        num for num in scores if num != scores[0]
    )  # First score not equal to min (first)
    for student in score_to_names[second_min]:
        print(student)  # Already alphabetical
