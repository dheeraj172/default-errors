#team name : default errors
def average_passing_grades(grades: list[int]) -> float:
    total = 0
    count = 0
    for grade in grades:
        if grade >= 50:
            total += grade
            count += 1
    if count == 0:
        return 0.0
    return total / count
