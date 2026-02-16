#team name: default error
def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:
        if is_student:
            return 12
        else:
            return 15
