from app.build_calendar import build_filtered_calendar_data
from app.save_json import save_json
from app.save_ics import save_ics
from constants.variables import ICS_URL, SELECTED_GROUP, START_FROM_DATE, OUTPUT_JSON

data = build_filtered_calendar_data(
    ics_url=ICS_URL,
    selected_group=SELECTED_GROUP,
    start_from_date=START_FROM_DATE,
)

save_json(data, OUTPUT_JSON)
save_ics(data, f"docs/group{SELECTED_GROUP}.ics")

print(f"Готово. Група {SELECTED_GROUP}. Збережено {len(data['events'])} подій у {OUTPUT_JSON}")