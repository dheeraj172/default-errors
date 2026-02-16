#team name: default errors
    
def convert_seconds(total_seconds: int) -> str:
    if total_seconds < 0 or total_seconds > 86400:
        raise ValueError("total_seconds must be between 0 and 86400")
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return str(minutes) + "m " + str(seconds) + "s"


