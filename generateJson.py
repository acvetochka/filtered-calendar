import json
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.request import urlopen
from icalendar import Calendar

from constants.group import GROUPS
from constants.variables import OUTPUT_JSON, ICS_URL, SELECTED_GROUP, START_FROM_DATE
from helpers.date_optimize import parse_hhmm, choose_base_date
from helpers.event import get_event_type



config = GROUPS[SELECTED_GROUP]

# with open(INPUT_ICS, "rb") as f:
#     cal = Calendar.from_ical(f.read())

with urlopen(ICS_URL) as response:
    cal = Calendar.from_ical(response.read())


original_name = str(cal.get("X-WR-CALNAME", "Calendar"))
original_timezone = str(cal.get("X-WR-TIMEZONE", "Europe/Kiev"))
original_description = str(cal.get("X-WR-CALDESC", ""))

TZ = ZoneInfo(original_timezone)

output = {
    "calendar_meta": {
        "prodid": "-//Alona Kuznietsova//LNA Filtered Calendar//UK",
        "version": str(cal.get("VERSION", "2.0")),
        "calscale": str(cal.get("CALSCALE", "GREGORIAN")),
        "method": str(cal.get("METHOD", "PUBLISH")),
        "name": f"{original_name}_Group{SELECTED_GROUP}",
        "timezone": original_timezone,
        "description": f"{original_description} - Group{SELECTED_GROUP}",
        "group": SELECTED_GROUP
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

    raw_dtstart = component.decoded("DTSTART") if component.get("DTSTART") else None
    raw_dtend = component.decoded("DTEND") if component.get("DTEND") else None

    base_date = choose_base_date(raw_dtstart, raw_dtend, config["date_source"])
    if not base_date:
        continue

    # Фільтр від певної дати
    if START_FROM_DATE and base_date < START_FROM_DATE:
        continue

    # Фільтр по днях тижня
    if base_date.weekday() not in config["days"]:
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
        "uid": f"{uid}-{base_date}-group{SELECTED_GROUP}@filtered.local",
        "weekday": base_date.weekday(),
        "source_date": config["date_source"],
    })

output["events"].sort(key=lambda e: e["dtstart"])

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Готово. Група {SELECTED_GROUP}. Збережено {len(output["events"])} подій у {OUTPUT_JSON}")