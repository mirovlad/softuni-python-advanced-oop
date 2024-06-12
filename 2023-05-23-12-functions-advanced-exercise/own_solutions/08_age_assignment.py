def age_assignment(*args, **kwargs):

    def get_age(name):
        if len(name) < 1:
            return

        if name[0] not in kwargs:
            return

        return kwargs[name[0]]

    person_ages = [(n, get_age(n)) for n in args]
    person_ages = sorted(person_ages, key=lambda p: p[0])

    return "\n".join(f"{p[0]} is {p[1]} years old." for p in person_ages)


print(age_assignment("Peter", "George", G=26, P=19))
# George is 26 years old.
# Peter is 19 years old.

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
# Amy is 22 years old.
# Bill is 61 years old.
# Willy is 36 years old.
