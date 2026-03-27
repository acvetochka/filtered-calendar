
from helpers.date_optimize import ensure_date

def get_event_type(summary: str) -> str:
    """
    Визначає тип події за назвою:
    - 'lesson' для 1. ... і подій без цифри на початку
    - 'homework' для 2. ...
    - None для всього іншого
    """
    summary = summary.strip()

    # if summary.startswith("1."):
    #     return "lesson"

    if summary.startswith("2."):
        return "homework"

    # if not summary[:1].isdigit():
    #     return "lesson"

    # return None
    return "lesson"


def is_common_friday_event(summary: str, raw_dtend) -> bool:
    if not raw_dtend:
        return False

    end_date = ensure_date(raw_dtend)
    if end_date.weekday() != 4:  # Friday
        return False

    summary_lower = summary.strip().lower()

    keywords = [
        "mashup",
        "додаткове заняття",
        "загальне заняття",
    ]

    return any(word in summary_lower for word in keywords)



