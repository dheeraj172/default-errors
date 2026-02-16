def convert_temperature(value: float, unit: text) -> float | text:
    if unit == 'C':
        result = (value * 9/5) + 32
    elif unit == 'F':
        result = (value - 32) * 5/9
    else:
        return "Invalid Unit"
    return round(result, 1)
