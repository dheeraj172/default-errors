def sanitize_email(raw_input: str) -> str:
    cleaned_email = raw_input.strip().lower()
    if cleaned_email == "" or cleaned_email.count("@") != 1:
        return "Invalid Email."
    return cleaned_email
