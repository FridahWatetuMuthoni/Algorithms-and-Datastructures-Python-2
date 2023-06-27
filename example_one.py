people = [
    ("Ned", "Eleanor"),
    ("Max", "Susan"),
    ("Susan", "Shelly"),
    ...
]


def find_person(people, child):
    for child_name, mom in people:  # O(n)
        if (child_name == child):  # O(1)
            return mom
    return None


print(people)
