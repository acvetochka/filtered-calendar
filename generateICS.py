import json
from datetime import datetime
from icalendar import Calendar, Event
from constants.variables import SELECTED_GROUP

with open(f"data/group{SELECTED_GROUP}.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)
    events = json_data["events"]
    metadata = json_data["calendar_meta"]
    # print(events)

cal = Calendar()
cal.add("prodid", metadata["prodid"])
cal.add("version", "2.0")
cal.add("calscale", "GREGORIAN")
cal.add("method", "PUBLISH")
cal.add("name", metadata["name"])
cal.add("timezone", metadata["timezone"])
cal.add("description", metadata["description"])

for item in events:
    event = Event()
    event.add("summary", item.get("summary", ""))
    event.add("description", item.get("description", ""))
    event.add("location", item.get("location", ""))
    event.add("status", item.get("STATUS", "CONFIRMED"))
    event.add("transp", item.get("TRANSP", "TRANSPARENT"))
    event.add("sequence", item.get("SEQUENCE", 0))
    
    if item.get("dtstart"):
        event.add("dtstart", datetime.fromisoformat(item["dtstart"]))
    if item.get("dtend"):
        event.add("dtend", datetime.fromisoformat(item["dtend"]))
    if item.get("uid"):
        event.add("uid", item["uid"])

    cal.add_component(event)

with open(f"output/group{metadata["group"]}.ics", "wb") as f:
    f.write(cal.to_ical())