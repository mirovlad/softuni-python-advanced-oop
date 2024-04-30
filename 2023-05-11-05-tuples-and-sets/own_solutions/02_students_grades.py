# My "natural" solution

from statistics import mean

record = {}

for _ in range(int(input())):
    name, grade = input().split()
    grade = float(grade)
    key = name
    if key not in record:
        record[key] = {
            "name": name,
            "grades": []
        }
    record[key]["grades"].append(grade)


for key, student in record.items():
    # This fails Judge's test
    # avg = mean(student["grades"])

    # This passes Judge's test
    avg = sum(student["grades"]) / len(student["grades"])

    # This works on my setup, but Judge says syntax error:
    # print(f"{student['name']} -> {' '.join([f"{x:.2f}" for x in student["grades"]])} (avg: {avg:.2f})")

    # This works both on my setup and in Judge:
    s_formatted_grades = ' '.join([f"{x:.2f}" for x in student["grades"]])
    print(f"{student['name']} -> {s_formatted_grades} (avg: {avg:.2f})")

