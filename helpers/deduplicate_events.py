def score_event(event: dict) -> tuple:
    description = event.get("description", "") or ""

    return (
        int(event.get("sequence", 0)),   # спочатку важливіша більша версія
        len(description),                # потім повніший description
    )


def deduplicate_events(events: list[dict]) -> list[dict]:
    unique = {}

    for event in events:
        key = (
            event.get("uid"),
            event.get("dtstart"),
            event.get("dtend"),
        )

        if key not in unique:
            unique[key] = event
            continue

        current = unique[key]

        if score_event(event) > score_event(current):
            unique[key] = event

    return sorted(unique.values(), key=lambda e: e["dtstart"])