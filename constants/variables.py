from dotenv import load_dotenv
from datetime import date
import os

load_dotenv()
MEET_URL = os.getenv("MEET_URL")
ICS_URL = os.getenv("ICS_URL")

# Обери групу тут:
SELECTED_GROUP = 1

# INPUT_ICS = "basic.ics"
OUTPUT_JSON = f"data/group{SELECTED_GROUP}.json"

# Опційний фільтр: з якої дати брати події
START_FROM_DATE = date(2026, 3, 9)
# START_FROM_DATE = date(2024, 5, 1)