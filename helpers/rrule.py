from datetime import datetime, date, timedelta
from typing import Iterable


def extract_until_date(component) -> date | None:
    """
    Дістає UNTIL з RRULE.
    Повертає date або None.
    """
    rrule_field = component.get("RRULE")
    if not rrule_field:
        return None

    until_values = rrule_field.get("UNTIL")
    if not until_values:
        return None

    until_value = until_values[0]

    if isinstance(until_value, datetime):
        return until_value.date()

    return until_value


def generate_weekly_dates_from_start(
    start_from_date: date,
    until_date: date,
    weekday: int,
) -> list[date]:
    """
    Генерує всі дати від start_from_date до until_date включно
    для заданого дня тижня.
    Monday=0 ... Friday=4
    """
    if start_from_date > until_date:
        return []

    days_ahead = (weekday - start_from_date.weekday()) % 7
    first_date = start_from_date + timedelta(days=days_ahead)

    dates = []
    current = first_date

    while current <= until_date:
        dates.append(current)
        current += timedelta(days=7)

    return dates