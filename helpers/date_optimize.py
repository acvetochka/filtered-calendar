from datetime import time, datetime, date

def parse_hhmm(value: str) -> time:
    hour, minute = map(int, value.split(":"))
    return time(hour, minute)

def ensure_date(value):
    """
    Якщо value = datetime -> повертаємо value.date()
    Якщо value = date -> повертаємо як є
    """
    if isinstance(value, datetime):
        return value.date()
    return value

def is_common_friday_event(raw_dtend) -> bool:
    if not raw_dtend:
        return False

    end_date = ensure_date(raw_dtend)
    # print(end_date, end_date.weekday())
    # П’ятниця
    if end_date.weekday() == 5:
        return True
    
def choose_base_date(raw_dtstart, raw_dtend, date_source: str) -> date | None:
     # Спільна п’ятнична подія — завжди беремо DTEND
    if is_common_friday_event(raw_dtend):
        return ensure_date(raw_dtend), "common_friday"
    
    if date_source == "DTSTART" and raw_dtstart:
        return ensure_date(raw_dtstart), "group"

    if date_source == "DTEND" and raw_dtend:
        return ensure_date(raw_dtend), "group"

    return None, None



