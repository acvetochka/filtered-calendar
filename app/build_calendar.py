
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.request import urlopen
from icalendar import Calendar

from constants.group import GROUPS
from helpers.date_optimize import parse_hhmm, choose_base_date
from helpers.event import get_event_type
from helpers.deduplicate_events import deduplicate_events


def build_filtered_calendar_data(
    ics_url: str,
    selected_group: int,
    start_from_date=None,
) -> dict:
    config = GROUPS[selected_group]

    with urlopen(ics_url) as response:
        cal = Calendar.from_ical(response.read())


    original_name = str(cal.get("X-WR-CALNAME", "Calendar"))
    original_timezone = str(cal.get("X-WR-TIMEZONE", "Europe/Kiev"))
    original_description = str(cal.get("X-WR-CALDESC", ""))

    TZ = ZoneInfo(original_timezone)

    output = {
        "calendar_meta": {
            "prodid": "-//Alona Kuznietsova//LNA Filtered Calendar//UK",
            "name": f"{original_name}_Group{selected_group}",
            "timezone": original_timezone,
            "description": f"{original_description} - Group{selected_group}",
            "group": selected_group
        },
        "events": []
    }

    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        summary = str(component.get("SUMMARY", "")).strip()
        description = str(component.get("DESCRIPTION", ""))
        location = str(component.get("LOCATION", ""))
        uid = str(component.get("UID", ""))
        sequence = int(component.get("SEQUENCE", 0))

        raw_dtstart = component.decoded("DTSTART") if component.get("DTSTART") else None
        raw_dtend = component.decoded("DTEND") if component.get("DTEND") else None

        base_date, event_mode = choose_base_date(raw_dtstart, raw_dtend, config["date_source"])
        if not base_date:
            continue

        if event_mode == "common_friday":
            print(base_date, event_mode)

        # Фільтр від певної дати
        if start_from_date and base_date < start_from_date:
            continue


        # Фільтр по днях тижня
        if event_mode == "group":
            if base_date.weekday() not in config["days"]:
                continue
        elif event_mode == "common_friday":
            pass
        else:
            continue

        event_type = get_event_type(summary)
        if event_type is None:
            continue

        if event_type == "lesson":
            start_str, end_str = config["lesson_time"]
        else:
            start_str, end_str = config["homework_time"]

        new_dtstart = datetime.combine(base_date, parse_hhmm(start_str), tzinfo=TZ)
        new_dtend = datetime.combine(base_date, parse_hhmm(end_str), tzinfo=TZ)

        output["events"].append({
            "summary": summary,
            "description": description,
            "location": location,
            "dtstart": new_dtstart.isoformat(),
            "dtend": new_dtend.isoformat(),
            "uid": f"{uid}-{base_date}-group{selected_group}@filtered.local",
            "weekday": base_date.weekday(),
            "source_date": config["date_source"],
            "sequence": sequence
        })
    
    output["events"] = deduplicate_events(output["events"])

    output["events"].sort(key=lambda e: e["dtstart"])
    return output