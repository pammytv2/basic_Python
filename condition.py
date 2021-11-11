def ticket(age):
    if age < 5:
        return 0
    else:
        return 100

def ticket2(age):
    if age < 5  or age >= 60:
        return 0
    elif age < 18:
        return 0
    else:
        return 100


def ticket3(age, is_local):
    if age < 5 or age >= 60 and is_local:
        return 0
    elif age < 18 and is_local:
        return 0
    else:
        return 100

print(ticket(3))
