import json

MAIN_COLOR = '#fd6a36'
HOVER_MAIN_COLOR = '#FD8B51'
TEXT_COLOR = '#243642'
WINDOW_COLOR = '#FCF8F3'

data = {
    "CTk": {
        "fg_color": MAIN_COLOR
    },
}

# Ghi vào file data.json
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
