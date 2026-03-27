# from constants.group import GROUPS
# from app.build_filtered_calendar_data import build_filtered_calendar_data
# from app.save_ics import save_ics
# from constants.variables import ICS_URL, START_FROM_DATE

# for group_id in GROUPS:
#     data = build_filtered_calendar_data(
#         ics_url=ICS_URL,
#         selected_group=group_id,
#         start_from_date=START_FROM_DATE,
#     )

#     save_ics(data, f"output/group{group_id}.ics")

import argparse
from constants.group import GROUPS
from constants.variables import ICS_URL, START_FROM_DATE

from app.build_calendar import build_filtered_calendar_data
from app.save_json import save_json
from app.save_ics import save_ics


def generate_group(group_id: int, with_json: bool = False):
    data = build_filtered_calendar_data(
        ics_url=ICS_URL,
        selected_group=group_id,
        start_from_date=START_FROM_DATE,
    )

    ics_path = f"output/group{group_id}.ics"
    save_ics(data, ics_path)

    if with_json:
        json_path = f"data/group{group_id}.json"
        save_json(data, json_path)

    print(f"✔ Group {group_id}: {len(data['events'])} events generated")


def main():
    parser = argparse.ArgumentParser(description="Generate filtered calendars")

    parser.add_argument(
        "group",
        help="group number (group1..group8) or 'all'"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="also save JSON output"
    )

    args = parser.parse_args()

    if args.group == "all":
        for group_id in GROUPS:
            generate_group(group_id, with_json=args.json)

    else:
        if not args.group.startswith("group"):
            raise ValueError("Use format: group1, group2, ...")

        group_id = int(args.group.replace("group", ""))

        if group_id not in GROUPS:
            raise ValueError(f"Unknown group: {group_id}")

        generate_group(group_id, with_json=args.json)


if __name__ == "__main__":
    main()